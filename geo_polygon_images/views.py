import requests
from django.contrib.gis.geos.geometry import GEOSGeometry
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SatelliteImage, Field
from .serializers import PolygonSerializer, FieldSerializer


class RetrieveImage(APIView):
    def post(self, request) -> Response:
        polygon_data = self.request.data.get("polygon")

        serializer = PolygonSerializer(data={"coordinates": polygon_data})
        if not serializer.is_valid():
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        polygon = serializer.save()

        newest_image = SatelliteImage.objects.filter(polygon=polygon).order_by("-datetime").first()

        if newest_image:
            return Response({"image_url": newest_image.image_url}, status=status.HTTP_200_OK)

        earth_search_api_url = "https://earth-search.aws.element84.com/v1"
        params = {"intersects": polygon_data}

        try:
            response = requests.get(earth_search_api_url, params=params)
            response.raise_for_status()
            image_url = response.json()["links"][3]["href"]

            SatelliteImage.objects.create(polygon=polygon, image_url=image_url)

            return Response({"image_url": image_url}, status=status.HTTP_200_OK)

        except requests.RequestException as error:
            return Response(
                {"error": f"Error fetching image: {error}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class CreateField(APIView):
    def post(self, request) -> Response:
        name = self.request.data.get("name")
        boundary = self.request.data.get("boundary")

        serializer = FieldSerializer(
            data={
                "name": name,
                "boundary": boundary
            }
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Field created successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class RetrieveIntersectingFields(APIView):
    def post(self, request) -> Response:
        polygon_data = self.request.data.get("polygon")

        polygon_geometry = GEOSGeometry(polygon_data)

        intersecting_fields = Field.objects.filter(boundary__intersects=polygon_geometry)

        serializer = FieldSerializer(intersecting_fields, many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

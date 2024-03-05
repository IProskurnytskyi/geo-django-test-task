import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SatelliteImage
from .serializers import FieldSerializer


class RetrieveSatelliteImage(APIView):
    @staticmethod
    def post(request) -> Response:
        polygon_data = request.data.get("polygon")

        serializer = FieldSerializer(data={"boundary": polygon_data})
        if not serializer.is_valid():
            return Response(
                {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
            )

        field = serializer.save()

        newest_image = SatelliteImage.objects.filter(field=field).order_by("-datetime").first()

        if newest_image:
            return Response({"image_url": newest_image.image_url}, status=status.HTTP_200_OK)

        earth_search_api_url = "https://earth-search.aws.element84.com/v1"
        params = {"intersects": polygon_data}

        try:
            response = requests.get(earth_search_api_url, params=params)
            response.raise_for_status()
            image_url = response.json()["links"][3]["href"]

            SatelliteImage.objects.create(field=field, image_url=image_url)

            return Response({"image_url": image_url}, status=status.HTTP_200_OK)

        except requests.RequestException as error:
            return Response(
                {"error": f"Error fetching image: {error}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

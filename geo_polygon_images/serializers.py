from rest_framework import serializers
from .models import Polygon, SatelliteImage, Field


class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygon
        fields = ("coordinates",)


class SatelliteImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SatelliteImage
        fields = ("polygon", "image_url", "datetime",)


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ("name", "boundary",)

from rest_framework import serializers
from .models import Polygon, SatelliteImage


class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygon
        fields = "__all__"


class SatelliteImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SatelliteImage
        fields = "__all__"

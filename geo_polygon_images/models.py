from django.contrib.gis.db import models


class Polygon(models.Model):
    coordinates = models.PolygonField()


class SatelliteImage(models.Model):
    polygon = models.ForeignKey(Polygon, on_delete=models.CASCADE)
    image_url = models.URLField()
    datetime = models.DateTimeField(auto_now_add=True)


class Field(models.Model):
    name = models.CharField(max_length=255)
    boundary = models.PolygonField()

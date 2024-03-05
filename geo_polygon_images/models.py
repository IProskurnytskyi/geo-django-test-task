from django.contrib.gis.db import models


class Polygon(models.Model):
    coordinates = models.PolygonField()


class SatelliteImage(models.Model):
    polygon = models.ForeignKey(Polygon, on_delete=models.CASCADE)
    image_url = models.URLField()
    datetime = models.DateTimeField(auto_now_add=True)

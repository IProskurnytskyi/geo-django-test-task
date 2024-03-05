from django.contrib.gis.db import models


class Field(models.Model):
    boundary = models.PolygonField()


class SatelliteImage(models.Model):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    image_url = models.URLField()
    datetime = models.DateTimeField(auto_now_add=True)

from django.urls import path

from views import RetrieveSatelliteImage


urlpatterns = [
    path(
        "retrieve-satellite-image/",
        RetrieveSatelliteImage.as_view(),
        name="retrieve-satellite-image"
    ),
]

app_name = "geo_polygon_images"

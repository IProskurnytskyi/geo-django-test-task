from django.urls import path

from .views import RetrieveSatelliteImage, CreateField


urlpatterns = [
    path(
        "retrieve-satellite-image/",
        RetrieveSatelliteImage.as_view(),
        name="retrieve-satellite-image",
    ),
    path(
        "create-field/",
        CreateField.as_view(),
        name="create-field"
    ),
]

app_name = "geo_polygon_images"

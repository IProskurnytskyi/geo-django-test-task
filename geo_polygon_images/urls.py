from django.urls import path

from .views import RetrieveImage, CreateField, RetrieveIntersectingFields


urlpatterns = [
    path(
        "retrieve-image/",
        RetrieveImage.as_view(),
        name="retrieve-image",
    ),
    path(
        "create-field/",
        CreateField.as_view(),
        name="create-field",
    ),
    path("retrieve-intersecting-fields/",
         RetrieveIntersectingFields.as_view(),
         name="retrieve-intersecting-fields",
    ),
]

app_name = "geo_polygon_images"

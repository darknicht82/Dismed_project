from django.urls import path
from . import views

app_name = "importacion"

urlpatterns = [
    path("", views.upload_matriz, name="upload_matriz"),
    path("registros/", views.registros_importacion, name="registros_importacion"),
]

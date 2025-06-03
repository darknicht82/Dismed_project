from django.urls import path
from . import views

urlpatterns = [
    path("", views.mostrar_matriz_dispositivos, name="mostrar_matriz_dispositivos"),
    path(
        "detalle/<int:idmatriz>/",
        views.mostrar_matriz_dispositivo,
        name="mostrar_matriz_dispositivo",
    ),
    path(
        "editar/<int:idmatriz>/",
        views.editar_matriz_dispositivo_view,
        name="editar_matriz_dispositivo_view",
    ),
    path(
        "unidad/<int:unidad_idudm>/",
        views.mostrar_matriz_por_unidad,
        name="mostrar_matriz_por_unidad",
    ),
]

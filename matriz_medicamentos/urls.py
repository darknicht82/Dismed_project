from django.urls import path
from . import views

urlpatterns = [
    path("", views.mostrar_matriz_medicamentos, name="mostrar_matriz_medicamentos"),
    path(
        "detalle/<int:idmatriz>/",
        views.mostrar_matriz_medicamento,
        name="mostrar_matriz_medicamento",
    ),
    path(
        "editar/<int:idmatriz>/",
        views.editar_matriz_medicamento_view,
        name="editar_matriz_medicamento_view",
    ),
]

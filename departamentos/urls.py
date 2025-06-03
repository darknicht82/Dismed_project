from django.urls import path

from . import views

urlpatterns = [
    path("", views.mostrar_departamentos, name="departamentos"),
    path("<int:iddepto>/", views.mostrar_departamento, name="mostrar_departamento"),
    path(
        "editar/<int:iddepto>/",
        views.editar_departamento_view,
        name="editar_departamento_view",
    ),
]

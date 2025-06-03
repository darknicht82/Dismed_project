from django.urls import path
from . import views

urlpatterns = [
    path("", views.mostrar_unidadesmd, name="mostrar_unidadesmd"),
    path("unidadmd/<int:idudm>/", views.mostrar_unidadmd, name="mostrar_unidadmd"),
    path(
        "editar/<int:idudm>/", views.editar_unidadmd_view, name="editar_unidadmd_view"
    ),
]

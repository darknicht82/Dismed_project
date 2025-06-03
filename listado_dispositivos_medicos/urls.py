from django.urls import path
from .views import listado_dispositivos_medicos_view, import_excel

urlpatterns = [
    path("", listado_dispositivos_medicos_view, name="listado_dispositivos_medicos"),
    path("import/", import_excel, name="import_excel"),
]

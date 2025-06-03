from django.db import models
from django.contrib.auth.models import User
from unidadesmd.models import UnidadMedica
import os
from datetime import datetime


def custom_upload_to(instance, filename):
    """
    Cambia el nombre del archivo subido para que incluya la fecha, hora y el nombre de la unidad médica.
    """
    # Extrae la extensión del archivo original
    extension = os.path.splitext(filename)[1]

    # Crea un nuevo nombre de archivo con fecha, hora y nombre de unidad
    new_filename = f"{instance.unidad_medica.nombre_unidad}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{extension}"

    return os.path.join("importaciones/", new_filename)


class RegistroImportacion(models.Model):
    fecha_importacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    archivo_importado = models.FileField(
        upload_to=custom_upload_to
    )  # Usar la función custom_upload_to
    version = models.IntegerField()  # La versión que se asignó durante esta importación
    unidad_medica = models.ForeignKey(UnidadMedica, on_delete=models.CASCADE)

    def __str__(self):
        return f"Importación realizada el {self.fecha_importacion} por {self.usuario}"

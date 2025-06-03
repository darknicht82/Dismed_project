from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from listado_dispositivos_medicos.models import ListadoDispositivosMedicos
from matriz_dispositivos.models import MatrizDispositivos


class Preseleccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    dispositivos = models.ManyToManyField(ListadoDispositivosMedicos)
    create_time = models.DateTimeField(auto_now_add=True)
    user_create = models.ForeignKey(
        User,
        related_name="preseleccion_created_by",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    modify_time = models.DateTimeField(auto_now=True)
    user_modify = models.ForeignKey(
        User,
        related_name="preseleccion_modified_by",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"Preselección de {self.usuario.username}"


class Estimacion(models.Model):
    preseleccion = models.ForeignKey(Preseleccion, on_delete=models.CASCADE)
    dispositivo = models.ForeignKey(
        ListadoDispositivosMedicos, on_delete=models.CASCADE
    )
    # Campos editables (por ejemplo, cantidad, precio, etc.)
    # ...
    priorizacion = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    user_create = models.ForeignKey(
        User,
        related_name="prepriorizacion_created_by",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    modify_time = models.DateTimeField(auto_now=True)
    user_modify = models.ForeignKey(
        User,
        related_name="prepriorizacion_modified_by",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"Estimación de {self.dispositivo.nombre}"


class Priorizacion(models.Model):
    pre_estimacion = models.ForeignKey(
        Estimacion, on_delete=models.CASCADE, related_name="priorizaciones"
    )
    matriz_dispositivo = models.ForeignKey(
        MatrizDispositivos, on_delete=models.CASCADE, related_name="priorizaciones"
    )
    # Campos necesarios para la priorización (por ejemplo, puntuación, ranking, etc.)
    # ...
    create_time = models.DateTimeField(auto_now_add=True)
    user_create = models.ForeignKey(
        User,
        related_name="priorizacion_created_by",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    modify_time = models.DateTimeField(auto_now=True)
    user_modify = models.ForeignKey(
        User,
        related_name="priorizacion_modified_by",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"Priorización de {self.pre_estimacion.dispositivo.nombre}"

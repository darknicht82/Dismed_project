from django.contrib.auth.models import User
from unidadesmd.models import UnidadMedica
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    unidad_medica = models.ForeignKey(
        UnidadMedica, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.user.username

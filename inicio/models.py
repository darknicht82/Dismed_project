from django.db import models


class InicioPermission(models.Model):
    class Meta:
        permissions = (("can_view_inicio", "Puede ver la página de inicio"),)
        # La siguiente línea asegura que este modelo no se cree en la base de datos
        managed = False

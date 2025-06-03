from django.db import models


class Departamentos(models.Model):
    iddepto = models.AutoField(primary_key=True)
    nombredept = models.CharField(max_length=255)

    class Meta:
        db_table = "departamentos"

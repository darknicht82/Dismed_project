from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import importacion.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("unidadesmd", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="RegistroImportacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha_importacion", models.DateTimeField(auto_now_add=True)),
                (
                    "archivo_importado",
                    models.FileField(upload_to=importacion.models.custom_upload_to),
                ),
                ("version", models.IntegerField()),
                (
                    "unidad_medica",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="unidadesmd.unidadmedica",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

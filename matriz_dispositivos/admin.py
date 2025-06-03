from django.contrib import admin
from .models import MatrizDispositivos


class MatrizDispositivosAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "unidad_medica",
        "version",
        "proyecc_saldo",
    )  # Agrega 'proyecc_saldo' a la lista
    # Resto de tus configuraciones del admin...


admin.site.register(MatrizDispositivos, MatrizDispositivosAdmin)

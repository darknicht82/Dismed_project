from django import forms
from .models import UserProfile
from unidadesmd.models import UnidadMedica
from django.contrib.auth.models import User, Group


class SelectUserForm(forms.Form):
    selected_user_id = forms.ModelChoiceField(
        queryset=User.objects.exclude(
            groups__name__in=["Administrador", "SuperAdmin"]
        ).order_by("username"),
        required=True,
        label="Seleccionar usuario",
    )


class AssignUnitForm(forms.Form):
    group = forms.ModelChoiceField(
        queryset=Group.objects.exclude(
            name__in=["Administrador", "SuperAdmin"]
        ).order_by("name"),
        required=True,
        label="Grupo",
    )
    unidad_medica = forms.ModelChoiceField(
        queryset=UnidadMedica.objects.all().order_by("nombre_unidad"),
        required=False,
        label="Unidad Médica",
    )

    class Meta:
        model = UserProfile
        fields = (
            "user",
            "unidad_medica",
        )

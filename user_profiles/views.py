from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AssignUnitForm, SelectUserForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache


@never_cache
@login_required
def assign_unit_view(request):
    selected_user = None
    current_group = None
    current_unit = None

    # Manejar el formulario para seleccionar el usuario
    select_user_form = SelectUserForm(request.POST or None)
    if select_user_form.is_valid():
        selected_user = select_user_form.cleaned_data["selected_user_id"]
        current_group = selected_user.groups.first()
        profile, _ = UserProfile.objects.get_or_create(user=selected_user)
        current_unit = profile.unidad_medica
        request.session["selected_user_id"] = selected_user.id  # Guardar en la sesión
        return redirect("assign_unit")  # Redirigir a la misma vista

    # Si hay un usuario seleccionado en la sesión, preparar el formulario de asignación
    if "selected_user_id" in request.session:
        selected_user_id = request.session["selected_user_id"]
        selected_user = User.objects.get(pk=selected_user_id)
        current_group = selected_user.groups.first()
        profile, _ = UserProfile.objects.get_or_create(user=selected_user)
        current_unit = profile.unidad_medica
        assign_unit_form = AssignUnitForm(
            initial={"group": current_group, "unidad_medica": current_unit}
        )
    else:
        assign_unit_form = None

    # Manejar el formulario de asignación si se envía
    if "assign_unit" in request.POST and assign_unit_form:
        assign_unit_form = AssignUnitForm(request.POST)
        if assign_unit_form.is_valid():
            selected_group = assign_unit_form.cleaned_data["group"]
            selected_unit = assign_unit_form.cleaned_data["unidad_medica"]

            selected_user.groups.clear()
            selected_user.groups.add(selected_group)
            profile.unidad_medica = selected_unit
            profile.save()

            messages.success(
                request,
                f"El Usuario: {selected_user} ha cambiado de {current_group} a {selected_group}.",
            )
            messages.success(
                request,
                f"Y su Unidad Médica ha cambiado de {current_unit} a {selected_unit}.",
            )
            return redirect("assign_unit")

    context = {
        "select_user_form": select_user_form,
        "assign_unit_form": assign_unit_form,
        "current_group": current_group,
        "current_unit": current_unit,
        "selected_user": selected_user,
    }
    return render(request, "assign_unit.html", context)

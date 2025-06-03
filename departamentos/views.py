from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect
from .models import (
    Departamentos,
)  # Asegúrate de importar el modelo Departamento correctamente
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@never_cache
@login_required
def mostrar_departamentos(request):
    departamentos = (
        Departamentos.objects.all()
    )  # Obtener todos los departamentos del modelo
    return render(request, "departamentos.html", {"departamentos": departamentos})


@never_cache
@login_required
def mostrar_departamento(request, iddepto):
    departamento = get_object_or_404(Departamentos, iddepto=iddepto)
    return render(request, "departamento.html", {"departamento": departamento})


@never_cache
@login_required
def editar_departamento_view(request, iddepto):
    departamento = get_object_or_404(Departamentos, iddepto=iddepto)

    if request.method == "POST":
        nombredept = request.POST.get("nombredept")  # Usa get para evitar KeyErrors

        if nombredept is not None:
            departamento.nombredept = nombredept
            departamento.save()

            messages.success(request, "Departamento actualizado correctamente.")
        else:
            messages.error(request, "El campo nombredept no está presente en el POST.")

        return redirect(
            "departamentos"
        )  # Asegúrate de que esta redirección es correcta
    else:
        return render(
            request, "editar_departamento.html", {"departamento": departamento}
        )

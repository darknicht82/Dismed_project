from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.cache import never_cache


@never_cache
@login_required
@permission_required("inicio.can_view_inicio")
def inicio_view(request):
    if request.user.is_authenticated:
        contenido = obtener_inicio()
        return render(request, "inicio.html", {"contenido": contenido})
    else:
        return redirect(
            "login"
        )  # Asegúrate de que 'login' sea el nombre correcto de la ruta de login en tu archivo urls.py


def obtener_inicio():
    # Lógica para obtener los datos de la página de inicio
    return "Contenido de la página de inicio"

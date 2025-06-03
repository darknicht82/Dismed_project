from django.shortcuts import render
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@never_cache
@login_required
def buscador_view(request):
    if request.method == "POST":
        # Obtener los datos del formulario de búsqueda y realizar la búsqueda
        query = request.POST.get("query")
        resultados = buscar(query)
        return render(request, "buscador.html", {"resultados": resultados})
    else:
        return render(request, "buscador.html")


@never_cache
@login_required
def buscar(query):
    # Lógica para realizar la búsqueda en la base de datos
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM unidadesmd WHERE nombre_unidad LIKE %s", [f"%{query}%"]
        )
        resultados = cursor.fetchall()
    return resultados

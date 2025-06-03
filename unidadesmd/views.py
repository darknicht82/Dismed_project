from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UnidadMedica
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@never_cache
@login_required
def mostrar_unidadesmd(request):
    unidadesmd = UnidadMedica.objects.all()
    return render(request, "unidadesmd.html", {"unidadesmd": unidadesmd})


@never_cache
@login_required
def mostrar_unidadmd(request, idudm):
    unidadmd = get_object_or_404(UnidadMedica, pk=idudm)
    return render(request, "unidadmd.html", {"unidadmd": unidadmd})


@never_cache
@login_required
def editar_unidadmd_view(request, idudm):
    unidadmd = get_object_or_404(UnidadMedica, pk=idudm)

    if request.method == "POST":
        campos_esperados = [
            "uni_codigo",
            "cod_um_as400",
            "cod_esigef",
            "cod_crp",
            "nombre_unidad",
            "nom_corto_unidad",
            "nivel_atencion",
            "tipologia_homo",
            "complejidad",
            "categ_establecimiento",
            "coord_provincial",
            "provincia",
            "cod_prov",
            "canton",
            "cod_cant",
            "parroquia",
            "cod_parroquia",
            "zona",
            "distrito",
        ]

        for campo in campos_esperados:
            if campo in request.POST:
                setattr(unidadmd, campo, request.POST[campo])

        unidadmd.save()
        messages.success(request, "Unidad médica actualizada correctamente.")
        return redirect(reverse("mostrar_unidadesmd"))

    return render(
        request,
        "editar_unidadmd.html",
        {
            "unidadmd": unidadmd,
            "editar_url": reverse("editar_unidadmd_view", args=[idudm]),
        },
    )

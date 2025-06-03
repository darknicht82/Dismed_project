from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MatrizDispositivos
from django.urls import reverse
from unidadesmd.models import UnidadMedica
from django.db import models
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@never_cache
@login_required
def mostrar_matriz_dispositivos(request):
    unidades_medicas = UnidadMedica.objects.annotate(
        ultima_version=models.Max("matrizdispositivos__version")
    ).order_by("nombre_unidad")
    return render(
        request,
        "vista_matrices_dispositivos.html",
        {"unidades_medicas": unidades_medicas},
    )


@never_cache
@login_required
def mostrar_matriz_dispositivo(request, idmatriz):
    matriz = get_object_or_404(MatrizDispositivos, pk=idmatriz)
    return render(request, "matriz_dispositivo.html", {"matriz": matriz})


@never_cache
@login_required
def mostrar_matriz_por_unidad(request, unidad_idudm):
    unidad = get_object_or_404(UnidadMedica, pk=unidad_idudm)
    ultima_version = MatrizDispositivos.objects.filter(unidad_medica=unidad).aggregate(
        models.Max("version")
    )["version__max"]
    matrices = MatrizDispositivos.objects.filter(
        unidad_medica=unidad, version=ultima_version
    ).order_by("item_nro")
    return render(
        request, "matrices_por_unidad.html", {"unidad": unidad, "matrices": matrices}
    )


@never_cache
@login_required
def editar_matriz_dispositivo_view(request, idmatriz):
    matriz = get_object_or_404(MatrizDispositivos, pk=idmatriz)

    if request.method == "POST":
        campos_esperados = [
            "unidad_medica",
            "version",
            "item_nro",
            "nom_subcomite",
            "nro_partida_pres",
            "nom_partida_pres",
            "cudim",
            "cod_iess",
            "cod_as400",
            "nom_generico",
            "espec_tec",
            "pres_unimed",
            "lvl_riesgo_suger",
            "lvl_aten_ia",
            "lvl_aten_ib",
            "lvl_aten_ic",
            "lvl_aten_ii",
            "lvl_aten_iii",
            "lvl_aten_aph",
            "espec_subespec",
            "consumo_prom_proyec",
            "perioci_consumo",
            "saldo_bodega_actual",
            "proyecc_saldo",
            "cant_pend_entre",
            "cod_proceso",
            "req_total_proyectado",
            "stock_seguridad",
            "cant_program_inicial",
            "cant_devol_prestam",
            "cant_final_required",
            "prec_unit_ref",
            "pres_ref_total",
            "dispo_dm",
            "lvl_abastec",
            "tip_proc_cp",
            "prim_cuatri_cant",
            "prim_cuatri_mont",
            "seg_cuatri_cant",
            "seg_cuatri_mont",
            "terc_cuatri_cant",
            "terc_cuatri_mont",
            "priorizacion",
            "observaciones",
            "create_time",
            "user_modify",
            "modify_time",
            "user_create",
        ]

        for campo in campos_esperados:
            if campo in request.POST:
                setattr(matriz, campo, request.POST[campo])

        matriz.save()
        messages.success(request, "Matriz de dispositivos actualizada correctamente.")
        return redirect(reverse("mostrar_matrices_dispositivos"))

    return render(
        request,
        "editar_matriz_dispositivo.html",
        {
            "matriz": matriz,
            "editar_url": reverse("editar_matriz_dispositivo_view", args=[idmatriz]),
        },
    )

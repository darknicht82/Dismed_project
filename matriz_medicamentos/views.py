from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MatrizMedicamentos
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@never_cache
@login_required
def mostrar_matriz_medicamentos(request):
    matrices = MatrizMedicamentos.objects.all()
    return render(request, "vista_matrices_medicamentos.html", {"matrices": matrices})


def mostrar_matriz_medicamento(request, idmatriz):
    matriz = get_object_or_404(MatrizMedicamentos, pk=idmatriz)
    return render(request, "matriz_medicamento.html", {"matriz": matriz})


def editar_matriz_medicamento_view(request, idmatriz):
    matriz = get_object_or_404(MatrizMedicamentos, pk=idmatriz)

    if request.method == "POST":
        campos_esperados = [
            "unidad_medica",
            "version",
            "matrix",
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
        messages.success(request, "Matriz de medicamentos actualizada correctamente.")
        return redirect(reverse("mostrar_matrices_medicamentos"))

    return render(
        request,
        "editar_matriz_medicamento.html",
        {
            "matriz": matriz,
            "editar_url": reverse("editar_matriz_medicamento_view", args=[idmatriz]),
        },
    )

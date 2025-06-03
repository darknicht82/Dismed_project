from django.db.models import Q


def get_nivel_atencion_queries(user):
    grupos_niveles = {
        "Operador 1": ["lvl_aten_ia", "lvl_aten_ib", "lvl_aten_ic"],
        "Operador 2": ["lvl_aten_ia", "lvl_aten_ib", "lvl_aten_ic", "lvl_aten_ii"],
        "Operador 3": [
            "lvl_aten_ia",
            "lvl_aten_ib",
            "lvl_aten_ic",
            "lvl_aten_ii",
            "lvl_aten_iii",
        ],
    }

    aph_optional = {
        "Operador 1": True,
        "Operador 2": True,
        "Operador 3": True,
    }

    queries = Q()
    for group in user.groups.all():
        niveles = grupos_niveles.get(group.name)
        if niveles:
            for nivel in niveles:
                queries |= Q(**{nivel: "X"})

            # Agregar consulta opcional para lvl_aten_aph si corresponde
            if aph_optional.get(group.name):
                queries |= Q(lvl_aten_aph="X") | Q(lvl_aten_aph="-")

    return queries

from django.shortcuts import render, redirect
from .forms import ImportExcelForm
from .models import ListadoDispositivosMedicos
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
import pandas as pd
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .utils import get_nivel_atencion_queries


@never_cache
@login_required
def validate_and_clean_data(data):
    # Lista de campos específicos para reemplazar NaN por un guión
    campos = [
        "cudim",
        "lvl_aten_ia",
        "lvl_aten_ib",
        "lvl_aten_ic",
        "lvl_aten_ii",
        "lvl_aten_iii",
        "lvl_aten_aph",
    ]

    # Reemplaza NaN en los campos específicos por un guión
    for campo in campos:
        data[campo].fillna("-", inplace=True)

    # Aquí añadir más validaciones y limpiezas según sea necesario
    return data


@never_cache
@login_required
def listado_dispositivos_medicos_view(request):
    nivel_atencion_queries = get_nivel_atencion_queries(request.user)
    dispositivos_list = ListadoDispositivosMedicos.objects.filter(
        nivel_atencion_queries
    ).order_by("item_nro")

    paginator = Paginator(dispositivos_list, 25)  # Muestra 25 dispositivos por página

    page_number = request.GET.get("page")
    try:
        dispositivos = paginator.page(page_number)
    except PageNotAnInteger:
        # Si la página no es un entero, entrega la primera página.
        dispositivos = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, entrega la última página de resultados.
        dispositivos = paginator.page(paginator.num_pages)

    return render(request, "listado.html", {"dispositivos": dispositivos})


@never_cache
@login_required
def import_excel(request):
    if request.method == "POST":
        form = ImportExcelForm(request.POST, request.FILES)
        if form.is_valid():
            excel_file = request.FILES["excel_file"]

            # Leer los datos desde el archivo Excel usando pandas
            data = pd.read_excel(excel_file)

            # Ordenar los datos por 'item_nro'
            data = data.sort_values(by="item_nro")
            data = validate_and_clean_data(data)

            for index, row in data.iterrows():
                try:
                    ListadoDispositivosMedicos.objects.create(
                        item_nro=row["item_nro"],
                        nom_subcomite=row["nom_subcomite"],
                        nro_partida_pres=row["nro_partida_pres"],
                        nom_partida_pres=row["nom_partida_pres"],
                        cudim=row["cudim"],
                        cod_iess=row["cod_iess"],
                        cod_as400=row["cod_as400"],
                        nom_generico=row["nom_generico"],
                        espec_tec=row["espec_tec"],
                        pres_unimed=row["pres_unimed"],
                        lvl_riesgo_suger=row["lvl_riesgo_suger"],
                        lvl_aten_ia=row["lvl_aten_ia"],
                        lvl_aten_ib=row["lvl_aten_ib"],
                        lvl_aten_ic=row["lvl_aten_ic"],
                        lvl_aten_ii=row["lvl_aten_ii"],
                        lvl_aten_iii=row["lvl_aten_iii"],
                        lvl_aten_aph=row["lvl_aten_aph"],
                        espec_subespec=row["espec_subespec"],
                    )
                except Exception as e:
                    error_message = (
                        f"Error al procesar la fila {index + 1}: {row}. Error: {str(e)}"
                    )
                    print(error_message)

                    # Si quieres identificar la columna específica donde ocurrió el error
                    for col_name, value in row.iteritems():
                        try:
                            # Intenta procesar cada valor de la columna
                            value = str(value)
                        except Exception as col_error:
                            print(
                                f"Error en la columna '{col_name}' con valor '{value}'. Error: {str(col_error)}"
                            )
                            break

            return redirect("listado_dispositivos_medicos")
    else:
        form = ImportExcelForm()

    return render(request, "upload_listado.html", {"form": form})

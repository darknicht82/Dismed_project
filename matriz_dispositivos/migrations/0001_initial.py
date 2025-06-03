from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("unidadesmd", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Periodo",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("periodicidad", models.CharField(max_length=255)),
                ("cantidad", models.IntegerField()),
                ("factor", models.IntegerField()),
                ("matriz_value", models.IntegerField()),
                ("stock_seguridad", models.IntegerField()),
            ],
            options={
                "db_table": "periodos",
            },
        ),
        migrations.CreateModel(
            name="MatrizDispositivos",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("version", models.IntegerField()),
                ("item_nro", models.IntegerField()),
                ("nom_subcomite", models.CharField(max_length=1000)),
                ("nro_partida_pres", models.IntegerField()),
                ("nom_partida_pres", models.CharField(max_length=255)),
                ("cudim", models.CharField(max_length=255)),
                ("cod_iess", models.CharField(max_length=255)),
                ("cod_as400", models.IntegerField()),
                ("nom_generico", models.CharField(max_length=255)),
                ("espec_tec", models.CharField(max_length=3000)),
                ("pres_unimed", models.CharField(max_length=255)),
                ("lvl_riesgo_suger", models.CharField(max_length=255)),
                ("lvl_aten_ia", models.CharField(max_length=255)),
                ("lvl_aten_ib", models.CharField(max_length=255)),
                ("lvl_aten_ic", models.CharField(max_length=255)),
                ("lvl_aten_ii", models.CharField(max_length=255)),
                ("lvl_aten_iii", models.CharField(max_length=255)),
                ("lvl_aten_aph", models.CharField(max_length=255)),
                ("espec_subespec", models.CharField(max_length=255)),
                ("consumo_prom_proyec", models.IntegerField()),
                ("perioci_consumo", models.CharField(max_length=255)),
                ("saldo_bodega_actual", models.IntegerField()),
                ("proyecc_saldo", models.IntegerField()),
                ("cant_pend_entre", models.IntegerField()),
                ("cod_proceso", models.CharField(max_length=255)),
                ("req_total_proyectado", models.IntegerField()),
                ("stock_seguridad", models.IntegerField()),
                ("cant_program_inicial", models.IntegerField()),
                ("cant_devol_prestam", models.IntegerField()),
                ("cant_final_required", models.IntegerField()),
                ("prec_unit_ref", models.DecimalField(decimal_places=4, max_digits=10)),
                (
                    "pres_ref_total",
                    models.DecimalField(decimal_places=4, max_digits=10),
                ),
                ("dispo_dm", models.IntegerField()),
                ("lvl_abastec", models.CharField(max_length=255)),
                ("tip_proc_cp", models.CharField(max_length=255)),
                ("prim_cuatri_cant", models.IntegerField()),
                (
                    "prim_cuatri_mont",
                    models.DecimalField(decimal_places=4, max_digits=10),
                ),
                ("seg_cuatri_cant", models.IntegerField()),
                (
                    "seg_cuatri_mont",
                    models.DecimalField(decimal_places=4, max_digits=10),
                ),
                ("terc_cuatri_cant", models.IntegerField()),
                (
                    "terc_cuatri_mont",
                    models.DecimalField(decimal_places=4, max_digits=10),
                ),
                ("priorizacion", models.BooleanField(default=False)),
                ("observaciones", models.CharField(max_length=255)),
                ("create_time", models.DateTimeField(auto_now_add=True)),
                ("user_modify", models.CharField(max_length=255)),
                ("modify_time", models.DateTimeField(auto_now=True)),
                ("user_create", models.CharField(max_length=255)),
                (
                    "unidad_medica",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="unidadesmd.unidadmedica",
                    ),
                ),
            ],
            options={
                "db_table": "matriz_dispositivos",
                "unique_together": {("cod_as400", "unidad_medica", "version")},
            },
        ),
    ]

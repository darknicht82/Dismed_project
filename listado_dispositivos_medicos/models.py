from django.db import models


class ListadoDispositivosMedicos(models.Model):
    id = models.AutoField(primary_key=True)
    item_nro = models.IntegerField()
    nom_subcomite = models.CharField(max_length=1000)
    nro_partida_pres = models.IntegerField()
    nom_partida_pres = models.CharField(max_length=255)
    cudim = models.CharField(max_length=255)
    cod_iess = models.CharField(max_length=255)
    cod_as400 = models.BigIntegerField()
    nom_generico = models.CharField(max_length=255)
    espec_tec = models.CharField(max_length=6000)
    pres_unimed = models.CharField(max_length=255)
    lvl_riesgo_suger = models.CharField(max_length=255)
    lvl_aten_ia = models.CharField(max_length=255)
    lvl_aten_ib = models.CharField(max_length=255)
    lvl_aten_ic = models.CharField(max_length=255)
    lvl_aten_ii = models.CharField(max_length=255)
    lvl_aten_iii = models.CharField(max_length=255)
    lvl_aten_aph = models.CharField(max_length=255)
    espec_subespec = models.CharField(max_length=255)

    class Meta:
        db_table = "listado_dispositivos_medicos"

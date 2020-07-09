from django.db import models
from cidades.models import Cidade, Uf
from django.db.models.signals import pre_save
from django.dispatch import receiver


class FeriadoEstadual(models.Model):
    uf = models.ForeignKey(Uf, on_delete=models.PROTECT)
    nome_feriado = models.CharField(max_length=150)
    data_feriado = models.DateField()
    mes_dia = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        unique_together = ('uf', 'data_feriado',)

@receiver(pre_save, sender=FeriadoEstadual)
def mes_dia(sender, instance, **kwargs):
    mes = str(instance.data_feriado.month)
    dia = str(instance.data_feriado.day)
    if len(mes) == 1:
        mes= '0'+mes
    if len(dia) == 1:
        dia = '0'+dia
    instance.mes_dia = mes +'-'+dia


class FeriadoMunicipal(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)
    nome_feriado = models.CharField(max_length=150)
    data_feriado = models.DateField()
    mes_dia = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        unique_together = ('cidade', 'data_feriado',)

@receiver(pre_save, sender=FeriadoMunicipal)
def mes_dia(sender, instance, **kwargs):
    mes = str(instance.data_feriado.month)
    dia = str(instance.data_feriado.day)
    if len(mes) == 1:
        mes= '0'+mes
    if len(dia) == 1:
        dia = '0'+dia
    instance.mes_dia = mes +'-'+dia


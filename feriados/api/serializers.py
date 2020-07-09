from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from feriados.models import FeriadoMunicipal
from feriados.models import FeriadoEstadual


class FeriadoUfSerializer(ModelSerializer):

    class Meta:
        model = FeriadoEstadual
        fields = ['uf', 'nome_feriado', 'data_feriado', 'mes_dia' ]

class FeriadoMuniSerializer(ModelSerializer):

    class Meta:
        model = FeriadoMunicipal
        fields = ['cidade', 'nome_feriado', 'data_feriado', 'mes_dia']






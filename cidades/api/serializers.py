from rest_framework import serializers, request
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from cidades.models import Cidade, Uf


class CidadeSerializer(ModelSerializer):

    class Meta:
        model = Cidade
        fields = ['codigo_ibge', 'nome']

class UfSerializer(ModelSerializer):

    class Meta:
        model = Uf
        fields = ['prefixo', 'uf']









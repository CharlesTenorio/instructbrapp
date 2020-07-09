from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from feriados.models import FeriadoEstadual, FeriadoMunicipal
from .serializers import FeriadoUfSerializer, FeriadoMuniSerializer


class FeraiadoUFViewSet(ModelViewSet):
    #TODO implentar seguracao
    #permission_classes = (IsAuthenticated,)
    queryset = FeriadoEstadual.objects.all()
    serializer_class = FeriadoUfSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome_feriado',)


class FeriadoMunicipalViewSet(ModelViewSet):
    #TODO implentar seguracao
    #permission_classes = (IsAuthenticated,)
    queryset = FeriadoMunicipal.objects.all()
    serializer_class = FeriadoMuniSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome_feriado',)



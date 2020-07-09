from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from cidades.models import Cidade, Uf
from .serializers import CidadeSerializer, UfSerializer


class CidadeViewSet(ModelViewSet):
    #TODO implentar seguracao
    #permission_classes = (IsAuthenticated,)
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome',)


class UfViewSet(ModelViewSet):
    #TODO implentar seguracao
    #permission_classes = (IsAuthenticated,)
    queryset = Uf.objects.all()
    serializer_class = UfSerializer



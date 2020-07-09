from rest_framework.response import Response
from rest_framework.views import APIView
from tools.tools import ImportCsvCidade


class CarregaCidadesAPIView(APIView):

    def post(self, request):
        """
         Carregar Dados das Cidades do Arquivo CSV do IBGE usando lib pandas
        """
        try:
            carrega = ImportCsvCidade()
            if carrega.inserir_cidades():
                return Response({'Dados': 'Cidades Carregadas com Sucesso'}, status=201)
        except Exception as e:
            return Response({'error': 'Dados nao carregados'}, status=500)

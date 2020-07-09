from rest_framework.response import Response
from rest_framework.views import APIView
from tools.tools import ImportCsvCidade, Feriados, ConsultarFeriados


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


class FeriadoConsultarAPIView(APIView):

    def get(self, request, codigo, data_feriado, format=None):
        '''passar o codigo do municiopo com 7 digiotos ou do estado com 2 digitos'''


        if codigo and data_feriado:
            feriado = ConsultarFeriados(codigo, data_feriado)
            msg, tem = feriado.feriado()
            if tem:
                return Response({'name':msg }, status=200)
            else:
                return Response({'name': msg}, status=404)






        """
         Carregar Dados das Cidades do Arquivo CSV do IBGE usando lib pandas
        """
        try:
            carrega = ImportCsvCidade()
            if carrega.inserir_cidades():
                return Response({'Dados': 'Cidades Carregadas com Sucesso'}, status=201)
        except Exception as e:
            return Response({'error': 'Dados nao carregados'}, status=500)


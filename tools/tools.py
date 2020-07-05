import pandas as pd
import os
from cidades.models import Cidade
from datetime import date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ImportCsv(object):
    def __init__(self):
        self.cidades = pd.read_csv(r'{}/cidades/municipios.csv'.format(BASE_DIR))

    def lista_cidade(self):
        return self.cidades.values.tolist()

    def inserir_cidades(self):
        try:
            cidades = Cidade.objects.first()
            if cidades:
                list_cidades = self.lista_cidade()
                Cidade.objects.bulk_create(list_cidades)
                return True
            else:
                return False
        except Exception:
            return False



class Feriados(object):
    '''
    Carnaval, Sexta-Feira Santa, Páscoa e Corpus Christi.
    '''

    def __init__(self, ano):

        self.ano = ano

    def retorna_pascoa(self):
        calculo1 = (19 * (self.ano % 19) + 24) % 30
        calculo2 = (2 * (self.ano % 4) + 4 * (self.ano % 7) + 6 * calculo1 + 5) % 7
        res = calculo1 + calculo2

        if res > 9:
            self.dia = res - 9
            # mes de abril
            mes = 4
        else:
            self.dia = res + 22
            mes = 3
        data_pascoa = date(self.ano, mes, self.dia)
        return data_pascoa


    def sexta_santa(self):
       data_pascoa = self.retorna_pascoa()
       data_sexta = date.fromordinal(data_pascoa.toordinal() - 2)
       return data_sexta

    def corpus(self):
        data_pascoa = self.retorna_pascoa()
        data_corpus = date.fromordinal(data_pascoa.toordinal() + 60)
        return data_corpus

    def carnaval(self):
        data_pascoa = self.retorna_pascoa()
        data_carnaval= date.fromordinal(data_pascoa.toordinal() - 47)
        return data_carnaval

    def natal(self):
        data_natal = date(self.ano, 12, 25)
        return data_natal

    def ano_novo(self):
        data_natal = date(self.ano, 1, 1)
        return data_natal

    def trabalhador(self):
        data_trabalhador = date(self.ano, 5, 1)
        return data_trabalhador

    def independencia(self):
        data_independencia = date(self.ano, 9, 7)
        return data_independencia

    def aparecida(self):
        data_aparecida = date(self.ano, 12, 10)
        return data_aparecida

    def finados(self):
        data_finados = date(self.ano, 11, 2)
        return data_finados

    def republica(self):
        data_republica = date(self.ano, 11, 15)
        return data_republica

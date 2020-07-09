import pandas as pd
import os
from cidades.models import Cidade, Uf
from datetime import datetime, date
from feriados.models import FeriadoEstadual, FeriadoMunicipal

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class LerCsv(object):
    def __init__(self):
        self.cidades = pd.read_csv(r'{}/cidades/municipios.csv'.format(BASE_DIR))

    def lista_cidade(self):
        return self.cidades.values.tolist()


class ImportCsvCidade(object):

    def remover_caracter(self, palavara):
        lista_remover = "`[]'"
        p = str(palavara)
        for i in range(0, len(lista_remover)):
            p = p.replace(lista_remover[i], "")

        return p

    def inserir_uf(self):
        try:
            ESTADOS = {
                '12': 'AC',
                '27': 'AL',
                '16': 'AP',
                '13': 'AM',
                '29': 'BA',
                '53': 'DF',
                '32': 'ES',
                '52': 'GO',
                '21': 'MA',
                '51': 'MT',
                '50': 'MS',
                '31': 'MG',
                '15': 'PA',
                '25': 'PB',
                '41': 'PR',
                '26': 'PE',
                '22': 'PI',
                '33': 'RJ',
                '24': 'RN',
                '43': 'RS',
                '11': 'RO',
                '14': 'RR',
                '42': 'SC',
                '35': 'SP',
                '28': 'SE',
                '17': 'TO'
            }

            lista_uf = []
            for k, v in ESTADOS.items():
                uniao = Uf(prefixo=str(k), uf=str(v))
                lista_uf.append(uniao)
            Uf.objects.bulk_create(lista_uf)
            return True
        except Exception as e:
            print(str(e))
            return False

    def inserir_cidades(self):
        try:
            cidades = Cidade.objects.first()
            if not cidades:
                import_cidade = LerCsv()
                cidades = import_cidade.lista_cidade()
                codigo_uf = ''
                codigo_cidade = ''
                nome_cidade = ''
                list_cidades = []
                for cidade in cidades:
                    codigo_uf = str(cidade[:2])
                    codigo_uf = codigo_uf[1:3]
                    uf = Uf.objects.get(pk=codigo_uf)
                    codigo_cidade = cidade[0:1]
                    codigo_cidade = self.remover_caracter(codigo_cidade)
                    nome_cidade = cidade[1:2]
                    nome_cidade = self.remover_caracter(nome_cidade)
                    c = Cidade(codigo_ibge=str(codigo_cidade), codito_uf=uf, nome=nome_cidade)
                    list_cidades.append(c)

                Cidade.objects.bulk_create(list_cidades)
                return True
            else:
                return False
        except Exception as e:
            print(str(e))
            return False


class Feriados(object):

    def __init__(self, ano):

        self.ano = ano
        self.nome_feriado= ""

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
        self.nome_feriado = 'Páscoa'
        return data_pascoa, self.nome_feriado

    def sexta_santa(self):
        data_pascoa = self.retorna_pascoa()
        data_sexta = date.fromordinal(data_pascoa.toordinal() - 2)
        self.nome_feriado= 'Sexta-Feira'
        return data_sexta, self.nome_feriado

    def corpus(self):
        data_pascoa = self.retorna_pascoa()
        data_corpus = date.fromordinal(data_pascoa.toordinal() + 60)
        self.nome_feriado='Sexta-Feira Santa'
        return data_corpus, self.nome_feriado

    def carnaval(self):
        data_pascoa = self.retorna_pascoa()
        data_carnaval = date.fromordinal(data_pascoa.toordinal() - 47)
        self.nome_feriado='Carnaval'
        return data_carnaval, self.nome_feriado

    def natal(self):
        data_natal = date(self.ano, 12, 25)
        self.nome_feriado = 'Natal'
        return data_natal, self.nome_feriado

    def ano_novo(self):
        data_ano = date(self.ano, 1, 1)
        self.nome_feriado = 'Ano novo'
        return data_ano, self.nome_feriado

    def trabalhador(self):
        data_trabalhador = date(self.ano, 5, 1)
        self.nome_feriado = 'Dia do Trabalhador'
        return data_trabalhador, self.nome_feriado

    def independencia(self):
        data_independencia = date(self.ano, 9, 7)
        self.nome_feriado= 'Independência'
        return data_independencia, self.nome_feriado

    def aparecida(self):
        data_aparecida = date(self.ano, 12, 10)
        self.nome_feriado='Nossa Senhora Aparecida'
        return data_aparecida, self.nome_feriado

    def finados(self):
        data_finados = date(self.ano, 11, 2)
        self.nome_feriado = 'Finados'
        return data_finados, self.nome_feriado

    def republica(self):
        data_republica = date(self.ano, 11, 15)
        self.nome_feriado = 'Proclamação da República'
        return data_republica, self.nome_feriado


class ConsultarFeriados(object):

    def __init__(self, codigo_ibge, data_feriado):
        self.codigo_ibge = codigo_ibge
        self.data_feriado = str(data_feriado)

        self.msg = ''
        self.tem_feriado = False

    def feriado(self):
        date_time_str = str(self.data_feriado)
        format_date = '%Y-%m-%d'
        date_time_obj = datetime.strptime(date_time_str, format_date).date()
        if len(self.codigo_ibge)==2 and len(self.data_feriado)==10:
            print('ok')

            feriado = FeriadoEstadual.objects.filter(uf=self.codigo_ibge, data_feriado=date_time_obj).first()
            if feriado:
                self.msg = feriado.nome_feriado
                self.tem_feriado=True

            else:
               self.msg = 'Nao tem feriado nessa data'
               self.tem_feriado = False

        if len(self.codigo_ibge)==7 and len(self.data_feriado)==10:
            feriado_muni = FeriadoMunicipal.objects.filter(cidade=self.codigo_ibge, data_feriado=date_time_obj).first()

            if feriado_muni:
                self.msg = feriado_muni.nome_feriado
                self.tem_feriado = True

            else:
               self.msg = 'Nao tem feriado nessa data'
               self.tem_feriado = False


        return self.msg, self.tem_feriado







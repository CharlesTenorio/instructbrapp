import pandas as pd
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class LerCsv(object):
    def __init__(self):
        self.cidades = pd.read_csv(r'{}/cidades/municipios.csv'.format(BASE_DIR))

    def lista_cidade(self):
        return self.cidades.values.tolist()

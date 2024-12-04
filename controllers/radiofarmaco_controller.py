import os
import pandas as pd
from controllers.controller_base import Controller_Base
from models.radiofarmaco_model import Radiofarmaco_Model

class Radiofarmaco_Controller(Controller_Base):
    def __init__(self):
        caminho_atual = os.path.dirname(__file__)
        caminho_dados = os.path.join(caminho_atual, "..", "data", "radiofarmacos.csv")
        super().__init__(pd.read_csv(caminho_dados), caminho_dados)
    
    def create(self, radiofarmaco: Radiofarmaco_Model):
        data = radiofarmaco.__dict__ #transforma a instância em um dicionário (chave-valor)
        super().create(data)

    def read(self, key_value, radiofarmaco: Radiofarmaco_Model):
        super().read(key_value, radiofarmaco)

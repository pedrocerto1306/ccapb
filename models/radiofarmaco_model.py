import pandas as pd
import string
from models.model_base import Model_Base

class Radiofarmaco(Model_Base):
  def __init__(self, id:int, nome:string, tipo:string, doseConcentracao:float, tempoInicioMedida:float, tempoMeiaVida:float, constanteDecaimento:float, lote:string, laboratorio:string, contraIndicacao:string, df : pd.DataFrame):
    super().__init__(df)
    self.id = id
    self.nome = nome
    self.tipo = tipo
    self.doseConcentracao = doseConcentracao #medido em mCi (micro curie)
    self.tempoInicioMedida = tempoInicioMedida
    self.tempoMeiaVida = tempoMeiaVida
    self.laboratorio = laboratorio
    self.contraIndicacao = contraIndicacao
    self.decaimento = calculaDecaimento(self)
    
    def calculaDecaimento(self):
        #TODO: Requisição à calculadora atomica de decaimento: https://sbmn.org.br/calculadora/
        return 0
        
    def addRadioFarmaco(self, dfRadio:pd.DataFrame):
        #TODO: Migrar para arquitetura MVC criada
        registroRadiofarmaco = { 
            'id': self.id,
            'nome': self.nome, 
            'tipo': self.tipo, 
            'doseConcentracao': self.doseConcentracao, 
            'tempoInicioMedida': self.tempoInicioMedida, 
            'tempoInicioMedida': self.tempoInicioMedida, 
            'laboratorio': self.laboratorio, 
            'contraIndicacao': self.contraIndicacao, 
            'decaimento': self.decaimento 
        }
        dfRadio._append(registroRadiofarmaco, ignore_index=True)
        return dfRadio
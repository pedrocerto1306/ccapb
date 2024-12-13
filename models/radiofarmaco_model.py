import pandas as pd
import string
import numpy as np
from models.model_base import *
from models.paciente_model import Paciente_Model

class Radiofarmaco_Model(Model_Base):
  def __init__(self, id:int, nome:string, tipo:string, doseConcentracao:float, horaChegada:float, horaAdministracao:float, tempoMeiaVida:float, laboratorio:string, contraIndicacao:string, df : pd.DataFrame):
    super().__init__(df)
    self.id = id
    self.nome = nome
    self.tipo = tipo
    self.doseConcentracao = doseConcentracao        #Medido em mCi (micro curie)
    self.horaChegada = horaChegada                  #Hora que o radiofármaco chegou no hospital
    self.horaAdministracao = horaAdministracao      #Hora que o radiofármaco foi administrado ao paciente
    self.tempoMeiaVida = tempoMeiaVida              #Tempo de meia vida do radiofármaco (em horas)
    self.laboratorio = laboratorio                  #Nome do laboratório que produz o medicamento
    self.contraIndicacao = contraIndicacao          #Lista de casos contra indicados (ex: suspeita de dengue)
    self.atividadeRemanescente = calcularAtividade(self)
    self.decaimento = calcular_decaimento_radioativo(self)
    

    # Função para calcular a atividade remanescente do radiofármaco
    def calcularAtividade(self): #Conversão de meia vida para segundos
        meia_vida_segundos = self.tempoMeiaVida * 3600
        diferenca_tempo = (self.horaAdministracao - self.horaChegada).total_seconds()
        fator_exponencial = -np.log(2) * diferenca_tempo / meia_vida_segundos #Calcula fator exponencial e calculo de decaimento
        atividade_inicial = 100 #Atividade inicial considerada %
        atividade_remanescente = atividade_inicial * np.exp(fator_exponencial) #Para calcular a atividade remanescente
        return atividade_remanescente
    
    def calcular_decaimento_radioativo(self):
        """
        Calcula a concentração restante do radiofármaco no momento da medição,
        com base na fórmula de decaimento radioativo: N(t) = N0 * (1/2)^(t/T).
        
        Returns:
            float: Concentração restante do radiofármaco após o tempo para início da medida.
        """
        
        tempo = self.horaAdministracao
        meia_vida = self.tempoMeiaVida
        if tempo <= 0 or meia_vida <= 0:
            return self.doseConcentracao

        # Fórmula de decaimento: N(t) = N0 * (1/2)^(t/T)
        concentracao_restante = self.doseConcentracao * (0.5 ** (tempo / meia_vida))
        return concentracao_restante
        
    def addRadioFarmaco(self, dfRadio:pd.DataFrame):
        #TODO: Migrar para arquitetura MVC criada
        registroRadiofarmaco = { 
            'id': self.id,
            'nome': self.nome, 
            'tipo': self.tipo, 
            'doseConcentracao': self.doseConcentracao, 
            'horaAdministracao': self.horaAdministracao, 
            'horaAdministracao': self.horaAdministracao, 
            'laboratorio': self.laboratorio, 
            'contraIndicacao': self.contraIndicacao, 
            'decaimento': self.decaimento 
        }
        dfRadio._append(registroRadiofarmaco, ignore_index=True)
        return dfRadio

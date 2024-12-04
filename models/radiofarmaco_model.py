import pandas as pd
import string
import numpy as np
from models.model_base import *

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
    self.decaimento = calculaDecaimento(self)
    

    # Função para calcular a atividade remanescente do radiofármaco
    def calcularAtividade(self): #Conversão de meia vida para segundos
        meia_vida_segundos = self.tempoMeiaVida * 3600
        diferenca_tempo = (self.horaAdministracao - self.horaChegada).total_seconds()
        fator_exponencial = -np.log(2) * diferenca_tempo / meia_vida_segundos #Calcula fator exponencial e calculo de decaimento
        atividade_inicial = 100 #Atividade inicial considerada %
        atividade_remanescente = atividade_inicial * np.exp(fator_exponencial) #Para calcular a atividade remanescente
        return atividade_remanescente
    
    #Mudar esse método para a classe paciente
    def calcular_tempo_afastamento(self, paciente: Paciente_Model): #meia_vida_horas, idade, atividade_desejada, peso_kg, altura_m
        meia_vida_dias = self.tempoMeiaVida / 24
        if paciente.idade <= 10:
            fator_idade = 5
        elif paciente.idade >= 66:
            fator_idade = 1
        else:
            fator_idade = 0.5
        tempo_afastamento = (1 / meia_vida_dias) * fator_idade * paciente.atividade_desejada * paciente.peso * paciente.altura
        tempo_afastamento = max(1, min(20, tempo_afastamento))
        return tempo_afastamento

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
            'horaAdministracao': self.horaAdministracao, 
            'horaAdministracao': self.horaAdministracao, 
            'laboratorio': self.laboratorio, 
            'contraIndicacao': self.contraIndicacao, 
            'decaimento': self.decaimento 
        }
        dfRadio._append(registroRadiofarmaco, ignore_index=True)
        return dfRadio

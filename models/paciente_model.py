from models.pessoa_model import Pessoa_Model

class Paciente_Model(Pessoa_Model):
   def __init__(self, id_paciente: int, cpf: str, plano_id: str, peso: float, altura: float, atividade_desejada: float):
      super().__init__(id_paciente)
      self.cpf = cpf
      self.plano_id = plano_id
      self.peso = peso
      self.altura = altura
      self.atividade_desejada = atividade_desejada
      
      
   def calcular_tempo_afastamento(self): #meia_vida_horas, idade, atividade_desejada, peso_kg, altura_m
      meia_vida_dias = self.tempoMeiaVida / 24
      if self.idade <= 10:
         fator_idade = 5
      elif self.idade >= 66:
         fator_idade = 1
      else:
         fator_idade = 0.5
      tempo_afastamento = (1 / meia_vida_dias) * fator_idade * self.atividade_desejada * self.peso * self.altura
      tempo_afastamento = max(1, min(20, tempo_afastamento))
      return tempo_afastamento

import datetime
from models.model_base import Model_Base

class Pessoa_Model(Model_Base):
  def __init__(self, nome: str, cpf: str, plano_id: str, dt_nasc: datetime, altura: float, peso: float):
    super().__init__(int(cpf.replace(".","").replace("-","")))
    self.nome = nome
    self.cpf = cpf
    self.plano_id = plano_id
    self.dt_nasc = dt_nasc
    self.altura = altura
    self.peso = peso

  def getName(self):
    print(self.nome)

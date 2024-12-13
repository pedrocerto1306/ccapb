import datetime

from models.pessoa_model import Pessoa_Model

class Medico_Model(Pessoa_Model):
   def __init__(self, nome: str, crm: int, cpf: str, plano_id: str, dt_nasc: datetime, peso: float, altura: float):
      super().__init__(nome, cpf, plano_id, dt_nasc, altura, peso)
      self.crm = crm
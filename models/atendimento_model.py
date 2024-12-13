import datetime

from models.model_base import Model_Base
from models.pessoa_model import Pessoa_Model

class Atendimento_Model(Model_Base):
  def __init__(self, id: int, hora_atendimento: datetime, cpf: str, plano_id: str, dt_nasc: datetime):
    self.id = id
    self.hora_atendimento = hora_atendimento
    self.cpf = cpf
    self.plano_id = plano_id
    self.dt_nasc = dt_nasc
    
    def __str__(self):
        return (
            f"Atendimento ID: {self.id}, Hora: {self.hora_atendimento}\n"
            f"CPF do Paciente: {self.cpf}\n"
            f"Identificador do plano de saude: {self.plano_id}\n"
            f"Data de nascimento do paciente: {self.dt_nasc}"
        )

from models.pessoa_model import Pessoa_Model

class Paciente_Model(Pessoa_Model):
   def __init__(self, id_paciente: int, cpf: str, plano_id: str, peso: float, altura: float):
    super().__init__(id_paciente)
    self.cpf = cpf
    self.plano_id = plano_id
    self.peso = peso
    self.altura = altura

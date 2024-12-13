from datetime import datetime
from models.model_base import Model_Base

class Agendamento_Model(Model_Base):
    def __init__(self, id: int, exame_id: int, paciente_id: int, medico_id: int,
                 data: datetime, radiofarmaco_id: int):
        super().__init__(id)
        self.exame_id = exame_id
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.data = data
        self.radiofarmaco_id = radiofarmaco_id

    def __str__(self):
        return (
            f"Agendamento ID: {self.id}\n"
            f"Exame: {self.exame_id}\n"
            f"Paciente: {self.paciente_id}\n"
            f"Médico: {self.medico_id}\n"
            f"Data: {self.data}\n"
            f"Radiofármaco: {self.radiofarmaco_id}"
        )

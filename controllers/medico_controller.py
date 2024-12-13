from typing import List, Dict, Any
from models.medico_model import Medico

class MedicoController:
    def __init__(self):
        self.id = None
        self.crm = None
        self.name = None
        self.medicos: List[Dict[str, Any]] = []

    def getDoctor(self):
        if not self.id:
            raise Exception("Por favor, identifique o médico")

        medico = next((m for m in self.medicos if m['id'] == self.id), None)
        if not medico:
            raise Exception("Médico não encontrado")

        return medico

    def editDoctor(self):
        if not self.id:
            raise Exception("Por favor, identifique o ID do médico a ser editado")
        if not self.crm and not self.name:
            raise Exception("Por favor, insira dados para editar.")

        medico = next((m for m in self.medicos if m['id'] == self.id), None)
        if not medico:
            raise Exception("Médico não encontrado")

        if self.crm:
            medico['crm'] = self.crm
        if self.name:
            medico['name'] = self.name

        index = self.medicos.index(next(m for m in self.medicos if m['id'] == self.id))
        self.medicos[index] = medico
        return medico

    def removeDoctor(self):
        if not self.id:
            raise Exception("Por favor, identifique o médico a ser removido.")

        if not any(m['id'] == self.id for m in self.medicos):
            raise Exception("Médico não encontrado")

        self.medicos = [m for m in self.medicos if m['id'] != self.id]

import uuid
from typing import List, Dict, Any

class Exame:
    def __init__(self, nome: str, radiofarmaco_id: str, dosagem: float):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.radiofarmaco_id = radiofarmaco_id
        self.dosagem = dosagem

    def criarExame(self) -> Dict[str, Any]:
        exame = {
            'id': self.id,
            'nome': self.nome,
            'radiofarmaco_id': self.radiofarmaco_id,
            'dosagem': self.dosagem
        }
        return exame

    def visualizarExame(self, id: str) -> Dict[str, Any]:
        exame = {
            'nome': self.nome,
            'radiofarmaco_id': self.radiofarmaco_id,
            'dosagem': self.dosagem
        }
        return exame

    def alterarExame(self, id: str, nome: str = '', radiofarmaco_id: str = '', dosagem: float = 0) -> Dict[str, Any]:
        df_exames: List[Dict[str, Any]] = []

        exame = next((e for e in df_exames if e['id'] == id), None)
        if not exame:
            raise ValueError(f"Exame with id {id} not found")

        novo_exame = {
            'nome': exame['nome'],
            'radiofarmaco_id': exame['radiofarmaco_id'],
            'dosagem': exame['dosagem']
        }

        if nome:
            novo_exame['nome'] = nome
        if radiofarmaco_id:
            novo_exame['radiofarmaco_id'] = radiofarmaco_id
        if dosagem:
            novo_exame['dosagem'] = dosagem

        index = df_exames.index(exame)
        df_exames[index] = novo_exame

        return novo_exame

    def removerExame(self, id: str) -> None:
        df_exames: List[Dict[str, Any]] = []
        df_exames = [e for e in df_exames if e['id'] != id]
        return None

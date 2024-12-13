from typing import List, Dict, Any
from models.exames_model import Exame

class ExamesController:
    def __init__(self):
        self.exames: List[Dict[str, Any]] = []

    def criar_exame(self, nome: str, radiofarmaco_id: str, dosagem: float) -> Dict[str, Any]:
        exame = Exame(nome, radiofarmaco_id, dosagem)
        exame_dict = {
            'id': exame.id,
            'nome': exame.nome,
            'radiofarmaco_id': exame.radiofarmaco_id,
            'dosagem': exame.dosagem
        }
        self.exames.append(exame_dict)
        return exame_dict

    def visualizar_exame(self, id: str) -> Dict[str, Any]:
        exame = next((e for e in self.exames if e['id'] == id), None)
        if not exame:
            raise ValueError(f"Exame with id {id} not found")
        return exame

    def alterar_exame(self, id: str, nome: str = '', radiofarmaco_id: str = '', dosagem: float = 0) -> Dict[str, Any]:
        exame = next((e for e in self.exames if e['id'] == id), None)
        if not exame:
            raise ValueError(f"Exame with id {id} not found")

        novo_exame = exame.copy()
        if nome:
            novo_exame['nome'] = nome
        if radiofarmaco_id:
            novo_exame['radiofarmaco_id'] = radiofarmaco_id
        if dosagem:
            novo_exame['dosagem'] = dosagem

        index = self.exames.index(exame)
        self.exames[index] = novo_exame
        return novo_exame

    def remover_exame(self, id: str) -> None:
        self.exames = [e for e in self.exames if e['id'] != id]

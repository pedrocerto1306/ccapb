from datetime import datetime

from models.model_base import Model_Base

class Exame_Model(Model_Base):
    def __init__(self, id_exame: int, nome_exame: str, descricao: str, data_realizacao: datetime, id_radiofarmaco: int):
        self.id_exame = id_exame
        self.nome_exame = nome_exame
        self.descricao = descricao
        self.data_realizacao = data_realizacao
        self.id_radiofarmaco = id_radiofarmaco

    def __str__(self):
        return (
            f"Exame ID: {self.id_exame}, Nome: {self.nome_exame}\n"
            f"Descrição: {self.descricao}\n"
            f"Data de Realização: {self.data_realizacao.strftime('%d/%m/%Y %H:%M')}\n"
            f"Radiofármaco: {self.radiofarmaco_utilizado}, Dose: {self.dose_radiofarmaco} MBq\n"
            f"Concentração Inicial: {self.concentracao_radiofarmaco} µCi/mL\n"
            f"Tempo para Medição: {self.tempo_para_inicio_medida} minutos\n"
            f"Concentração Restante: {self.calcular_decaimento_radioativo():.2f} µCi/mL"
        )

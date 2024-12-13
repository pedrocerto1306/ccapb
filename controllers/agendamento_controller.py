import os
import pandas as pd
from datetime import datetime
from controllers.controller_base import Controller_Base
from models.agendamento_model import Agendamento_Model

class Agendamento_Controller(Controller_Base):
    def __init__(self):
        caminho_atual = os.path.dirname(__file__)
        caminho_dados = os.path.join(caminho_atual, "..", "data", "agendamentos.csv")
        super().__init__(pd.read_csv(caminho_dados), caminho_dados)

        self.df_exames = pd.read_csv(os.path.join(caminho_atual, "..", "data", "exames.csv"))
        self.df_planos = pd.read_csv(os.path.join(caminho_atual, "..", "data", "planos.csv"))
        self.df_pacientes = pd.read_csv(os.path.join(caminho_atual, "..", "data", "pacientes.csv"))
        self.df_medicos = pd.read_csv(os.path.join(caminho_atual, "..", "data", "medicos.csv"))
        self.df_radiofarmacos = pd.read_csv(os.path.join(caminho_atual, "..", "data", "radiofarmacos.csv"))

    def marcar_agendamento(self, exame, paciente, medico, data: datetime):
        if paciente.cpf == medico.cpf:
            raise Exception('Um médico não pode marcar um exame para si mesmo.')

        dados_paciente = self.df_pacientes[self.df_pacientes['id'] == paciente.id]
        if dados_paciente.empty:
            raise Exception('Esse paciente não existe.')

        dados_medico = self.df_medicos[self.df_medicos['id'] == medico.id]
        if dados_medico.empty:
            raise Exception('Esse médico não existe.')

        dados_radiofarmaco = self.df_radiofarmacos[self.df_radiofarmacos['id'] == exame.radiofarmaco_id]
        if dados_radiofarmaco.empty:
            raise Exception('Esse radiofármaco não existe.')

        # verifica se data é válida
        if data <= datetime.now():
            raise Exception('Por favor, escolha uma data válida.')

        # restrições
        if dados_radiofarmaco['restricao_gravidez'].values[0] and paciente.gravidez:
            raise Exception('O paciente não pode realizar esse exame devido à restrição de gravidez.')

        if paciente.idade <= dados_radiofarmaco['restricao_idade'].values[0]:
            raise Exception('O paciente não pode realizar esse exame devido à restrição de idade.')

        # verifica cobertura do plano
        dados_plano = self.df_planos[self.df_planos['id'] == paciente.plano.id]
        if exame.id not in dados_plano['exames_cobertos'].values[0]:
            raise Exception('Este exame não é coberto pelo plano do paciente.')

        agendamento = {
            'exame_nome': exame.nome,
            'exame_id': exame.id,
            'medico_solicitante_id': medico.id,
            'medico_solicitante_nome': medico.nome,
            'paciente_id': paciente.id,
            'paciente_nome': paciente.nome,
            'plano_id': paciente.plano.id,
            'plano_nome': paciente.plano.nome,
            'convenio_id': paciente.plano.convenio.id,
            'convenio_nome': paciente.plano.convenio_nome,
            'radiofarmaco_id': exame.radiofarmaco_id,
            'radiofarmaco_nome': dados_radiofarmaco['nome'].values[0],
            'radiofarmaco_dosagem': dados_radiofarmaco['dosagem'].values[0],
            'data': data
        }

        self.create(agendamento)
        return agendamento

    def cancelar_agendamento(self, id):
        self.delete(id, Agendamento)

    def buscar_agendamentos(self, paciente_id=None, medico_id=None, radiofarmaco_id=None):
        query = self.df.copy()

        if paciente_id:
            query = query[query['paciente_id'] == paciente_id]
        if medico_id:
            query = query[query['medico_solicitante_id'] == medico_id]
        if radiofarmaco_id:
            query = query[query['radiofarmaco_id'] == radiofarmaco_id]

        return query

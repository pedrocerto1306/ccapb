from datetime import datetime

class Agendamento:
  def __init__(self, nome: str, cpf: str, plano_id: str, dt_nasc: date, altura: float, peso: float):
    # TODO randomizar self id
    self.id

  def marcarAgendamento(exame, paciente, medico, data: datetime):
    # talvez passar somente cpf do paciente e crm do medico ao inves de passar o objeto inteiro? mesma coisa pro radiofarmaco
    # alias, nem precisa do radiofarmaco nos params. o exame é que deve dizer qual é o radiofarmaco.
    df_exames = []
    df_planos = []
    df_pacientes = []
    df_medicos = []
    df_radiofarmacos = []

    # confere se paciente e medico sao mesma pessoa
    if(paciente.cpf == medico.cpf):
      throw(Exception: 'Um médico não pode marcar um exame para si mesmo.')

    # confere se médico, paciente e radiofármaco existem e estão corretos
    dados_paciente = df_pacientes[paciente.id]
    if !paciente :
      throw(Exception: 'Esse paciente não existe.')

    dados_medico = df_medicos[medico.id]
    if !medico :
      throw(Exception: 'Esse médico não existe.')

    dados_radiofarmaco = df_radiofarmacos[radiofarmaco.id]
    if !radiofarmaco :
      throw(Exception: 'Esse radiofármaco não existe.')


    # confere se data não é anterior a agora
    agora = datetime.now()

    if(datetime <= agora):
      throw(Exception: 'Por favor, escolha uma data válida.')

    # confere se ha restricoes da condicao do paciente (idade, gravidez)

    restricoes_radiofarmaco = radiofarmaco.restricoes

    if(radiofarmaco.restricao_gravidez && paciente.gravidez):
      throw(Exception: 'O paciente não pode realizar esse exame devido à restrição de gravidez.')

    if(paciente.idade <= radiofarmaco.restricao_idade):
      throw(Exception: 'O paciente não pode realizar esse exame devido à restrição de idade.')

    # confere se o plano cobre
    dados_plano = df_plano[paciente.plano.id]
    if(dados_plano.exames.includes(exame.id)) # corrigir essa linha aqui, certeza que logica/sintaxe nao funcionam.


    agendamento = {
        exame_nome
        exame_id

        medico_solicitante_id: medico.id
        medico_solicitante_nome: medico.nome

        paciente_id: paciente.id
        paciente_nome: paciente.nome

        plano_id: plano.id
        plano_nome: plano.nome
        convenio_id: plano.convenio.id
        convenio_nome: plano.convenio_nome

        radiofarmaco_id: radiofarmaco.id
        radiofarmaco_nome: radiofarmaco.nome
        radiofarmaco_dosagem: radiofarmaco.dosagem

        data: data

        }

    df.append(agendamento)

  def cancelarAgendamento(id):
    # TODO import dataframe
    df.drop([id], inplace=True)

    # TODO ensure dataframe file is updated

  def buscarAgendamentos(paciente = '', medico = '', radiofarmaco = ''):
    # TODO conectar a df agendamentos
    df_agendamentos = []

    # retorna um ou mais agendamentos de acordo com os parâmetros oferecidos
    # em dataframes, será que dá pra usar algo como o JOIN para múltiplos parâmetros? Incluindo parametros vazios?

    query = '´´´SELECT * FROM df_agendamentos'
    if(paciente):
      query += 'WHERE pacience_id = paciente.id'
    if(medico):
      query =+ 'WHERE medico_id = medico.id'
    if(radiofarmaco):
      query =+ 'WHERE radiofarmaco_id = radiofarmaco.id'
    query += '´´´'


    result = pandas.read_sql_query(query)

    logger(result)

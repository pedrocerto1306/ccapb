import uuid

class Exame:
  def __init__(self, nome: str, radiofarmaco_id, dosagem: float):
    # TODO randomizar self id
    self.nome = nome
    self.radiofarmaco_id = radiofarmaco_id
    self.dosagem = dosagem

  def criarExame(self):
    id = uuid.uuid4()

    exame = {
      id: id,
      nome: self.nome,
      radiofarmaco_id: self.radiofarmaco_id,
      dosagem: self.dosagem
    }

    return exame;

  def visualizarExame(self, id):
      exame = {
          nome: self.nome
          radiofarmaco_id = self.radiofarmaco_id
          dosagem = self.dosagem
      }
      return exame


  def alterarExame(self, id, nome: str = '', radiofarmaco_id: str = '', dosagem: float = 0):
    # TODO acessa df de exames
    df_exames = []

    # busca exame por id na df
    exame = df_exames[id]
    novo_exame = {
        nome: exame.nome
        radiofarmaco_id: exame.radiofarmaco.id
        dosagem: exame.dosagem
    }

    if nome {
       novo_exame.nome: nome
    }
    if radiofarmaco_id {
        novo_exame.radiofarmaco_id: radiofarmaco.id
    }
    if dosagem {
        novo_exame.dosagem: dosagem
    }

    df_exames.replace((exame, novo_exame))

    return df_exames[id]

  def removerExame(self, id):
    # TODO acessa df de exames
    df_exames = []
    df_exames.drop(df_exames.index[[id]])

    return;

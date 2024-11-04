import string
import pandas as pd
from models.model_base import Model_Base

#Classe base dos controllers. Apresenta estrutura base para as operações de CRUD utilizando dataframes pandas.
class Controller_Base():
    def __init__(self, df: pd.DataFrame, database_path: string):
        self.df = df
        self.database_path = database_path

    def create(self, dados:dict):
        #Adiciona um registro no dataframe, baseado no dicionario fornecido (importante ressaltar que o dicionario deve coincidir com a estrutura de colunas do dataframe)
        self.df = self.df._append(dados, ignore_index=True)
        self.df.to_csv(self.database_path, header=True, index=False)
        
    def read(self, key_value, model:Model_Base):
        #Dada uma chave, retorna o registro dela na tabela
        return self.df.loc[self.df[model.id] == key_value]

    def update(self, primary_key, key_value, updates):
        #Busca registro com o id especificado e atualiza-o no dataframe
        record_index = self.df[self.df[primary_key] == key_value].index
        if not record_index.empty:
            for column, new_value in updates.items():
                self.df.loc[record_index, column] = new_value
                self.df.to_csv(self.database_path)
            print(f"Registro {primary_key} atualizado para {key_value} com sucesso!")
        else:
            raise(f"Erro de atualizacao de dados: nenhum registro para a chave {key_value} foi encontrado no dataframe fornecido.")

    def delete(self, key_value, model:Model_Base):
        #Basicamente atualiza o dataframe para apenas as correspondencias de registros cujo id não é o key_value passado
        self.df = self.df[self.df[model.id] != key_value]
        self.df.to_csv(self.database_path)

    #Método adicional para encontrar o id de um registro novo (última linha)
    def getNewIndex(self):
        return self.df.shape[0]
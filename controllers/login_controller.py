import os
import pandas as pd
from controllers.controller_base import Controller_Base
from models.login_model import Login_Model

class Login_Controller(Controller_Base):
    def __init__(self):
        caminho_atual = os.path.dirname(__file__)
        caminho_dados = os.path.join(caminho_atual, "..", "data", "users.csv")
        super().__init__(pd.read_csv(caminho_dados), caminho_dados)
    
    def create(self, login: Login_Model):
        data = login.__dict__
        super().create(data)
    
    def read(self, login: Login_Model):
        #Sobrecarga do método "read" original para buscar o "username" ao invés do "id", como de padrão.
        register_exists = (self.df['username'] == login.username).any()
        if register_exists:
            return self.df.loc[self.df['username'] == login.username]
        else:
            return pd.DataFrame()
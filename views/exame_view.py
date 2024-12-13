import os
import customtkinter as ctk
import pandas as pd
from models.exame_model import Exame_Model
from views.base_view import Base_View
from controllers.controller_base import Controller_Base

class Exame_View(ctk.CTkFrame, Base_View):
    def __init__(self, parent):
        super().__init__(parent)
        # self.title("Cadastro de Paciente")
        # self.geometry("400x400")
        caminho_atual = os.path.dirname(__file__)
        caminho_dados = os.path.join(caminho_atual, "..", "data", "exames.csv")
        self.controller = Controller_Base(pd.read_csv(caminho_dados), caminho_dados)


        # Armazena os campos de entrada
        self.inputs = {}

        # Labels e inputs
        self.create_label_and_entry("ID Exame:", "id_exame")
        self.create_label_and_entry("Nome do Exame:", "nome_exame")
        self.create_label_and_entry("Descricao do Exame:", "descricao")
        self.create_label_and_entry("Data de realizacao:", "data_realizacao")
        self.create_label_and_entry("Identificacao do Radiofarmaco:", "id_radiofarmaco")

        # Botão para criar o objeto
        self.submit_button = ctk.CTkButton(self, text="Cadastrar Exame", command=self.cadastrar)
        self.submit_button.pack(pady=20)

    def create_label_and_entry(self, label_text, attribute_name):
        label = ctk.CTkLabel(self, text=label_text)
        label.pack(pady=5)
        entry = ctk.CTkEntry(self)
        entry.pack(pady=5)
        self.inputs[attribute_name] = entry
    
    def getObject(self):
        return Exame_Model(self.inputs["id_exame"].get(), self.inputs["nome_exame"].get(), self.inputs["descricao"].get(), self.inputs["data_realizacao"].get(), self.inputs["id_radiofarmaco"].get())
    
    def cadastrar(self):
        objDict = self.getObject().__dict__
        self.controller.create(objDict)
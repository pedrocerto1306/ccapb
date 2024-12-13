import customtkinter as ctk
from models.atendimento_model import Atendimento_Model
from views.base_view import Base_View
from controllers.controller_base import Controller_Base
import os
import pandas as pd

class Atendimento_View(ctk.CTkFrame, Base_View):
    def __init__(self, parent):
        super().__init__(parent)
        # self.title("Cadastro de Paciente")
        # self.geometry("400x400")
        caminho_atual = os.path.dirname(__file__)
        caminho_dados = os.path.join(caminho_atual, "..", "data", "atendimentos.csv")
        self.controller = Controller_Base(pd.read_csv(caminho_dados), caminho_dados)

        # Armazena os campos de entrada
        self.inputs = {}

        # Labels e inputs
        self.create_label_and_entry("ID do Atendimento:", "id")
        self.create_label_and_entry("Horario do atendimento:", "hora_atendimento")
        self.create_label_and_entry("CPF do Paciente:", "cpf")
        self.create_label_and_entry("ID do plano de saude:", "plano_id")
        self.create_label_and_entry("Data de nascimento do paciente:", "dt_nasc")

        # Botão para criar o objeto
        self.submit_button = ctk.CTkButton(self, text="Cadastrar Atendimento", command=self.cadastrar)
        self.submit_button.pack(pady=20)

    def create_label_and_entry(self, label_text, attribute_name):
        label = ctk.CTkLabel(self, text=label_text)
        label.pack(pady=5)
        entry = ctk.CTkEntry(self)
        entry.pack(pady=5)
        self.inputs[attribute_name] = entry
    
    def getObject(self):
        return Atendimento_Model(self.inputs["id"].get(), self.inputs["hora_atendimento"].get(), self.inputs["cpf"].get(), self.inputs["plano_id"].get(), self.inputs["dt_nasc"].get())

    def cadastrar(self):
        objDict = self.getObject().__dict__
        self.controller.create(objDict)
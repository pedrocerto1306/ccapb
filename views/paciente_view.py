import os
import customtkinter as ctk
import pandas as pd
from models.paciente_model import Paciente_Model
from controllers.controller_base import Controller_Base
from views.base_view import Base_View

class Paciente_View(ctk.CTkFrame, Base_View):
    def __init__(self, parent):
        super().__init__(parent)
        # self.title("Cadastro de Paciente")
        # self.geometry("400x400")
        caminho_atual = os.path.dirname(__file__)
        caminho_dados = os.path.join(caminho_atual, "..", "data", "pacientes.csv")
        self.controller = Controller_Base(pd.read_csv(caminho_dados), caminho_dados)

        # Armazena os campos de entrada
        self.inputs = {}

        # Labels e inputs
        self.create_label_and_entry("ID Paciente:", "id_paciente")
        self.create_label_and_entry("CPF:", "cpf")
        self.create_label_and_entry("Plano ID:", "plano_id")
        self.create_label_and_entry("Peso (kg):", "peso")
        self.create_label_and_entry("Altura (m):", "altura")

        # Botão para criar o objeto
        self.submit_button = ctk.CTkButton(self, text="Cadastrar Paciente", command=self.cadastrar)
        self.submit_button.pack(pady=20)

    def create_label_and_entry(self, label_text, attribute_name):
        label = ctk.CTkLabel(self, text=label_text)
        label.pack(pady=5)
        entry = ctk.CTkEntry(self)
        entry.pack(pady=5)
        self.inputs[attribute_name] = entry

    def getObject(self):
        return Paciente_Model(self.inputs["id_paciente"].get(), self.inputs["cpf"].get(), self.inputs["plano_id"].get(), self.inputs["peso"].get(), self.inputs["altura"].get(), self.inputs["atividade_desejada"].get())

    def cadastrar(self):
        objDict = self.getObject().__dict__
        self.controller.create(objDict)
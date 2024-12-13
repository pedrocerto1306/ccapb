import os
import customtkinter as ctk
import pandas as pd

from models.radiofarmaco_model import Radiofarmaco_Model
from controllers.controller_base import Controller_Base
from views.base_view import Base_View

class Radiofarmacos_View(ctk.CTkFrame, Base_View):
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
        # id:int, nome:string, tipo:string, doseConcentracao:float, horaChegada:float, horaAdministracao:float, tempoMeiaVida:float, 
        # laboratorio:string, contraIndicacao:string, df : pd.DataFrame
        self.create_label_and_entry("ID do Radiofarmaco:", "id")
        self.create_label_and_entry("Nome do Radiofarmaco:", "nome")
        self.create_label_and_entry("Tipo:", "tipo")
        self.create_label_and_entry("Concentracao da Dose (mCi - micro curie)", "doseConcentracao")
        self.create_label_and_entry("Hora da chegada:", "horaChegada")
        self.create_label_and_entry("Hora da admnistracao:", "horaAdministracao")
        self.create_label_and_entry("Tempo de meia vida:", "tempoMeiaVida")
        self.create_label_and_entry("Laboratorio:", "laboratorio")
        self.create_label_and_entry("Contra indicacao:", "contraIndicacao")

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
        return Radiofarmaco_Model(self.inputs["id"].get(), self.inputs["nome"].get(), self.inputs["tipo"].get(), self.inputs["doseConcentracao"].get(), self.inputs["horaChegada"].get(), self.inputs["horaAdministracao"].get(), self.inputs["tempoMeiaVida"].get(), self.inputs["laboratorio"].get(), self.inputs["contraIndicacao"].get())

    def cadastrar(self):
        objDict = self.getObject().__dict__
        self.controller.create(objDict)
import customtkinter as ctk
from tkinter import messagebox

from views.paciente_view import Paciente_View
from views.base_view import Base_View

class Menu_View(ctk.CTkFrame, Base_View):
    def __init__(self, parent):
        super().__init__(parent)
        # self.title("SGDR - Menu")
        # self.geometry("1080x720")

        self.usernameLabel = ctk.CTkLabel(self, text="Menu")
        self.usernameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        #Acesso pacientes
        self.pacienteButton = ctk.CTkButton(self, text="Pacientes", command=parent.show_frame(Paciente_View))
        self.pacienteButton.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

        #Acesso exames
        self.exameButton = ctk.CTkButton(self, text="Exames", command=parent.show_frame(Exame_View))
        self.exameButton.grid(row=2, column=0, columnspan=4, padx=20, pady=1, sticky="ew")

        #Acesso aos atendimentos
        self.atendimentoButton = ctk.CTkButton(self, text="Atendimentos", command=parent.show_frame(Atendimento_View))
        self.atendimentoButton.grid(row=3, column=0, columnspan=4, padx=20, pady=1, sticky="ew")

        #Acesso aos funcionarios
        self.funcionarioButton = ctk.CTkButton(self, text="Funcionarios", command=parent.show_frame(Funcionario_View))
        self.funcionarioButton.grid(row=4, column=0, columnspan=4, padx=20, pady=1, sticky="ew")

        
        
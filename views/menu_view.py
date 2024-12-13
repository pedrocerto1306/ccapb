import customtkinter as ctk
from tkinter import messagebox

from views.paciente_view import Paciente_View
from views.base_view import Base_View
from views.exame_view import Exame_View
from views.atendimento_view import Atendimento_View
from views.funcionario_view import Funcionario_View
from views.radiofarmacos_view import Radiofarmacos_View

class Menu_View(ctk.CTkFrame, Base_View):
    def __init__(self, parent):
        super().__init__(parent)
        # self.title("SGDR - Menu")
        # self.geometry("1080x720")

        self.usernameLabel = ctk.CTkLabel(self, text="Menu", anchor="center")
        self.usernameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        #Acesso pacientes
        self.pacienteButton = ctk.CTkButton(self, text="Pacientes", command=lambda: parent.show_frame(Paciente_View))
        self.pacienteButton.grid(row=1, column=0, columnspan=4, padx=500, pady=20, sticky="ew")

        #Acesso exames
        self.exameButton = ctk.CTkButton(self, text="Exames", command=lambda: parent.show_frame(Exame_View))
        self.exameButton.grid(row=2, column=0, columnspan=4, padx=500, pady=20, sticky="ew")

        #Acesso aos atendimentos
        self.atendimentoButton = ctk.CTkButton(self, text="Atendimentos", command=lambda: parent.show_frame(Atendimento_View))
        self.atendimentoButton.grid(row=3, column=0, columnspan=4, padx=500, pady=20, sticky="ew")

        #Acesso aos funcionarios
        self.funcionarioButton = ctk.CTkButton(self, text="Funcionarios", command=lambda: parent.show_frame(Funcionario_View))
        self.funcionarioButton.grid(row=4, column=0, columnspan=4, padx=500, pady=20, sticky="ew")
        
        #Acesso aos Radiofarmacos
        self.funcionarioButton = ctk.CTkButton(self, text="Radiofarmacos", command=lambda: parent.show_frame(Radiofarmacos_View))
        self.funcionarioButton.grid(row=5, column=0, columnspan=4, padx=500, pady=20, sticky="ew")
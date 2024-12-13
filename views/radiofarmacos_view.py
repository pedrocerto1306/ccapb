import customtkinter as ctk
from views.base_view import Base_View

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#dimensões da tela:
largura, altura = 1080, 720

class Radiofarmacos_View(ctk.CTk, Base_View):
    def __init__(self, parent):
        super().__init__(parent)
        # self.title("Sistema de gerenciamento de doses de radiofármacos")
        # self.geometry("1080x720")

        #Rótulo e input de texto para o Nome do radiofármaco
        self.nameLabel = ctk.CTkLabel(self, text="Nome radiofármaco")
        self.nameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.nameEntry = ctk.CTkEntry(self, placeholder_text="Flúor-18")
        self.nameEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Botão para inclusão do radiofármaco na base de dados (csv)
        self.addRadiopharmaceutical = ctk.CTkButton(self, text="Adicionar Radiofármaco", anchor="center", command=super().show_message("teste"))
        self.addRadiopharmaceutical.grid(row=5, column=1, columnspan=2, padx=20, pady=20, sticky="ew")
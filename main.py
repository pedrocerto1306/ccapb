import customtkinter as ctk
import pandas as pd

from views.login import Login

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#dimensões da tela:
largura, altura = 1080, 720

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Sistema de gerenciamento de doses de radiofármacos")
        self.geometry(f"{largura}x{altura}")

        #Rótulo e input de texto para o Nome do radiofármaco
        self.nameLabel = ctk.CTkLabel(self, text="Nome radiofármaco")
        self.nameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.nameEntry = ctk.CTkEntry(self, placeholder_text="Flúor-18")
        self.nameEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Botão para inclusão do radiofármaco na base de dados (csv)
        self.addRadiopharmaceutical = ctk.CTkButton(self, text="Adicionar Radiofármaco")
        self.addRadiopharmaceutical.grid(row=5, column=1, columnspan=2, padx=20, pady=20, sticky="ew")


if __name__ == "__main__":
    #Carrega os dados iniciais
    dfRadiofarmacos = pd.read_csv('./data/radiofarmacos.csv')
    dfLogin = pd.read_csv('./data/users.csv')
    
    #Cria interface base
    app = Login()
    app.mainloop()
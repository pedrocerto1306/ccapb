import customtkinter as ctk

from controllers.login_controller import Login_Controller
from models.login_model import Login_Model

class Login(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.login_controller = Login_Controller()
        self.title("SGDR - Login")
        self.geometry("320x225")

        #Rótulo e input de texto para o nome de usuário
        self.usernameLabel = ctk.CTkLabel(self, text="Nome de usuário")
        self.usernameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.usernameEntry = ctk.CTkEntry(self, placeholder_text="user_01")
        self.usernameEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.passwordLabel = ctk.CTkLabel(self, text="Senha")
        self.passwordLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.passwordEntry = ctk.CTkEntry(self, placeholder_text="pass_01", show="*")
        self.passwordEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Botao de login
        self.loginButton = ctk.CTkButton(self, text="Entrar", command=self.commitLogin)
        self.loginButton.grid(row=2, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

        self.signUpButton = ctk.CTkButton(self, text="Cadastrar", command=self.signUp)
        self.signUpButton.grid(row=3, column=0, columnspan=4, padx=20, pady=1, sticky="ew")

    def commitLogin(self):
        database_register = self.login_controller.read(Login_Model(0, self.usernameEntry.get(), self.passwordEntry.get()))
        if database_register.empty:
            print(f"Usuario nao cadastrado: {self.usernameEntry.get()}")
        else:
            #TODO: Validar senha
            print(f"Bem-vindo: {self.usernameEntry.get()}")
            #TODO: Implementar troca de tela para painel principal
        return
    
    def signUp(self):
        new_id = self.login_controller.getNewIndex()
        self.login_controller.create(Login_Model(new_id, self.usernameEntry.get(), self.passwordEntry.get()))

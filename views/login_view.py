import customtkinter as ctk

from controllers.login_controller import Login_Controller
from models.login_model import Login_Model
from views.base_view import Base_View
from views.menu_view import Menu_View

from tkinter import messagebox

class Login_View(ctk.CTkFrame, Base_View):
    def __init__(self, parent):
        super().__init__(parent)
        self.login_controller = Login_Controller()
        self.parent = parent
        # self.title("SGDR - Login")
        # self.geometry("1080x720")

        #Rótulo e input de texto para o nome de usuário
        self.usernameLabel = ctk.CTkLabel(self, text="Nome de usuário", anchor="center")
        self.usernameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.usernameEntry = ctk.CTkEntry(self, placeholder_text="user_01")
        self.usernameEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        self.passwordLabel = ctk.CTkLabel(self, text="Senha", anchor="center")
        self.passwordLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        self.passwordEntry = ctk.CTkEntry(self, placeholder_text="pass_01", show="*")
        self.passwordEntry.grid(row=1, column=1, columnspan=3, padx=20, pady=20, sticky="ew")

        #Botao de login
        self.loginButton = ctk.CTkButton(self, text="Entrar", anchor="center", command=self.commitLogin)
        self.loginButton.grid(row=2, column=0, columnspan=4, padx=20, pady=10, sticky="ew")

        self.signUpButton = ctk.CTkButton(self, text="Cadastrar", anchor="center", command=self.signUp)
        self.signUpButton.grid(row=3, column=0, columnspan=4, padx=20, pady=1, sticky="ew")

    def commitLogin(self):
        database_register = self.login_controller.read(Login_Model(0, self.usernameEntry.get(), self.passwordEntry.get()))
        if database_register.empty:
            messagebox.showinfo("Atencao", "Usuario nao cadastrado: {}".format(self.usernameEntry.get()))
        elif database_register.loc[database_register["username"] == self.usernameEntry.get(), "password"].values[0] == self.passwordEntry.get():
            messagebox.showinfo("Atencao", "Bem-vindo: {}".format(self.usernameEntry.get()))
            self.parent.show_frame(Menu_View)
        else:
            messagebox.showinfo("Atencao", "{}: sua senha está incorreta!".format(self.usernameEntry.get()))
        return
    
    def signUp(self):
        new_id = self.login_controller.getNewIndex()
        self.login_controller.create(Login_Model(new_id, self.usernameEntry.get(), self.passwordEntry.get()))
        messagebox.showinfo("Atencao", "Novo usuario cadastrado: {}".format(self.usernameEntry.get()))

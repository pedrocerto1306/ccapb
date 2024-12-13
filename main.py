import pandas as pd
import os
import customtkinter as ctk

from views.base_view import Base_View
from views.login_view import Login_View
from views.menu_view import Menu_View

if __name__ == "__main__":
    #Carrega os dados iniciais
    diretorioRaiz = os.path.dirname(os.path.abspath(__file__))

    dfRadiofarmacos = pd.read_csv('{}\\data\\radiofarmacos.csv'.format(diretorioRaiz))
    dfLogin = pd.read_csv('{}\\data\\users.csv'.format(diretorioRaiz))
    
    #Cria interface base
    app = Base_View()
    app.show_frame(Menu_View)
    app.mainloop()
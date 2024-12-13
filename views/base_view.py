import customtkinter as ctk
import string
import datetime
from tkinter import messagebox

from numpy import double

class Base_View(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Radiofármacos")
        self.geometry("1080x720")
        # Frame atual
        self.current_frame = None

    def show_frame(self, frame_class):
        # Remove o frame atual, se existir
        if self.current_frame is not None:
            self.current_frame.destroy()

        # Cria o novo frame
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)
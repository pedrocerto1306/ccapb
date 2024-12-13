import customtkinter as ctk
from models.paciente_model import Paciente_Model
from views.base_view import Base_View

class Paciente_View(ctk.CTkFrame, Base_View):
    def __init__(self, parent):
        super().__init__(parent)
        # self.title("Cadastro de Paciente")
        # self.geometry("400x400")

        # Labels e inputs
        self.create_label_and_entry("ID Paciente:", "id_paciente")
        self.create_label_and_entry("CPF:", "cpf")
        self.create_label_and_entry("Plano ID:", "plano_id")
        self.create_label_and_entry("Peso (kg):", "peso")
        self.create_label_and_entry("Altura (m):", "altura")

        # Botão para criar o objeto
        self.submit_button = ctk.CTkButton(self, text="Cadastrar Paciente", command=self.create_paciente)
        self.submit_button.pack(pady=20)

        # Armazena os campos de entrada
        self.inputs = {}

    def create_label_and_entry(self, label_text, attribute_name):
        label = ctk.CTkLabel(self, text=label_text)
        label.pack(pady=5)
        entry = ctk.CTkEntry(self)
        entry.pack(pady=5)
        self.inputs[attribute_name] = entry

    def create_paciente(self):
        try:
            # Coleta os dados dos campos
            id_paciente = int(self.inputs["id_paciente"].get())
            cpf = self.inputs["cpf"].get()
            plano_id = self.inputs["plano_id"].get()
            peso = float(self.inputs["peso"].get())
            altura = float(self.inputs["altura"].get())

            # Cria o objeto Paciente_Model
            paciente = Paciente_Model(id_paciente, cpf, plano_id, peso, altura)
            print("Paciente cadastrado com sucesso:", vars(paciente))

            # Mensagem de sucesso
            ctk.CTkLabel(self, text="Paciente cadastrado com sucesso!", text_color="green").pack(pady=5)
        except Exception as e:
            # Mensagem de erro
            ctk.CTkLabel(self, text=f"Erro: {str(e)}", text_color="red").pack(pady=5)
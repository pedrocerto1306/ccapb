import random
from datetime import datetime, timedelta

pacientes = [] #lista para ser adicionado os pacientes

def gerar_data_nascimento(min_idade=0, max_idade=100):#Irá gerar uma data de nascimento aleatória dentro desse intervalo de tempo, usando em média 100 anos
    hoje = datetime.today()#pega a data atual
    idade = random.randint(min_idade, max_idade)
    delta_dias = idade * 365 + random.randint(0, 365)
    data_nascimento = hoje - timedelta(days=delta_dias)
    return data_nascimento

def calcular_idade(data_nascimento): #calculo da idade com base na data de nascimento do paciente
    hoje = datetime.today()
    return hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))

def gerar_cpf():#irá gerar um cpf fictício no padão de 11 dígitos.
    def calc_dv(cpf): #para calcular os dígitos verificadores do CPF
        peso = list(range(len(cpf) + 1, 1, -1))
        soma = sum(int(a) * b for a, b in zip(cpf, peso))
        dv = 11 - (soma % 11)
        return dv if dv < 10 else 0

    cpf_base = [random.randint(0, 9) for _ in range(9)]
    cpf_base.append(calc_dv(cpf_base))
    cpf_base.append(calc_dv(cpf_base))
    return ''.join(map(str, cpf_base))

def gerar_dados_paciente(): #foi necessário colocar nomes ficticios no código para que seja gerado os dados á partir disso, primeiramente 20 pacientes
    nomes = ["Ana Silva", "João Souza", "Carlos Oliveira", "Mariana Costa", "Pedro Santos",
             "Renata Lima", "Paulo Ferreira", "Juliana Mendes", "Felipe Castro", "Camila Rocha","Maísa de Souza","Vinicius Rodrigues","Maria Gomes",
             "Luiz Henrique", "Daniel de Souza", "Victor Hugo", "Guilherme Rodrigues", "Roberto Rodrigues","Valentina Rocha", "Luiza Oliveira"]
    nome = random.choice(nomes)
    cpf = gerar_cpf()
    data_nascimento = gerar_data_nascimento(0, 100)
    idade = calcular_idade(data_nascimento)
    peso = round(random.uniform(40, 120), 1)
    altura = round(random.uniform(1.5, 2.0), 2)
    id_paciente = ''.join(random.choices('0123456789abcdef', k=8))

    return {
        "ID": id_paciente,
        "Nome": nome,
        "CPF": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
        "Data de Nascimento": data_nascimento.strftime('%d/%m/%Y'),
        "Idade": idade,
        "Peso (kg)": peso,
        "Altura (m)": altura,
        "IMC": round(peso / (altura ** 2), 2) #Calculo do IMC(indice de massa corporal, importante para saber se a pessoa está no peso ideal para a faixa etária)
    }

def popular_pacientes_iniciais():#faixa inicial de pacientes ficticios em 20 pessoas, mas isso pode ser alterado para uma lista maior
    global pacientes
    pacientes = [gerar_dados_paciente() for _ in range(20)]

def adicionar_paciente():#para adicionar pacientes manualmente, sendo assim possível, criar novos pacientes sem ser gerados aleatóriamente.
    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o CPF do paciente (somente números): ")
    data_nascimento = input("Digite a data de nascimento (dd/mm/yyyy): ")
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))
    id_paciente = ''.join(random.choices('0123456789abcdef', k=8))

    # Calcula idade e IMC
    data_nascimento_dt = datetime.strptime(data_nascimento, '%d/%m/%Y')
    idade = calcular_idade(data_nascimento_dt)
    imc = round(peso / (altura ** 2), 2)

    paciente = {
        "ID": id_paciente,
        "Nome": nome,
        "CPF": cpf,
        "Data de Nascimento": data_nascimento,
        "Idade": idade,
        "Peso (kg)": peso,
        "Altura (m)": altura,
        "IMC": imc
    }
    pacientes.append(paciente)
    print("Paciente adicionado com sucesso!")

def excluir_paciente():#para excluir algum paciente manualmente
    id_paciente = input("Digite o ID do paciente que deseja excluir: ")
    global pacientes
    paciente_encontrado = next((p for p in pacientes if p["ID"] == id_paciente), None)
    if paciente_encontrado:
        pacientes = [p for p in pacientes if p["ID"] != id_paciente]
        print("Paciente excluído com sucesso!")
    else:
        print("Paciente não encontrado.")

#Essa função irá apresentar todos os pacientes presentes na lista no momento que for chamada, ou caso não conste nenhum paciente apresentará
#a mensagem de que nenhum paciente foi cadastrado.
def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for paciente in pacientes:
            print(paciente)

#função para criar um menu interativo, onde será possível, adicionar um paciente manualmente, excluir pacientes,
# ver a lista de pacientes já adicionados
def menu():
    while True:
        print("\n1. Adicionar paciente manualmente")
        print("2. Excluir paciente")
        print("3. Listar pacientes")
        print("4. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_paciente()
        elif escolha == "2":
            excluir_paciente()
        elif escolha == "3":
            listar_pacientes()
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    popular_pacientes_iniciais()
    menu()

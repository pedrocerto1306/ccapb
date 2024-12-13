import random

medicos = []# Lista com os médicos fictícios, inicialmente com 10, mas pode-se adicionar mais se necessário.

def gerar_cpf():  #Gerador de CPF fictício no padrão de 11 dígitos
    def calc_digverificador(cpf):# Função para calcular o dígito verificador do CPF
        peso = list(range(len(cpf) + 1, 1, -1))
        soma = sum(int(a) * b for a, b in zip(cpf, peso))
        dv = 11 - (soma % 11)
        return dv if dv < 10 else 0

    cpf_base = [random.randint(0, 9) for _ in range(9)]
    cpf_base.append(calc_digverificador(cpf_base))
    cpf_base.append(calc_digverificador(cpf_base))
    return ''.join(map(str, cpf_base))

def gerar_crm(estado_abreviado=None):# Função para gerar um número aleatório de CRM
    numero_crm = random.randint(10000, 99999)
    if estado_abreviado:
        return f"CRM-{estado_abreviado}-{numero_crm}"
    return f"CRM-{numero_crm}"

def gerar_nome_medico():# Lista de nomes fictícios de médicos.
    nomes = ["Dra. Ana Luiza", "Dra. Joana Souza", "Dra. Carminha de Oliveira",
             "Dr. Mario da Costa", "Dr. Pedro Nascimento", "Dra. Renata Rodrigues",
             "Dr. Paulo Pereira", "Dra. Luciana Mendes", "Dr. João de Castro", "Dr. Denis Rocha"]
    return random.choice(nomes)

def gerar_id_medico():# Função para gerar um ID único para o médico.
    return ''.join(random.choices('0123456789abcdef', k=8))

def gerar_dados_medico():#Função para gerar dados de um médico fictício
    nome = gerar_nome_medico()
    cpf = gerar_cpf()
    estado = random.choice(["SP", "RJ", "MG", "BA", "RS", "AC", "AL", "AP", "AM",
                            "CE", "DF", "ES", "GO", "MA", "MT", "MS", "PA",
                            "PB", "PR", "PE", "PI", "RN", "RO", "RR", "SC", "SE", "TO"])  # Escolher um estado aleatório
    crm = gerar_crm(estado)
    id_medico = gerar_id_medico()

    return {
        "ID": id_medico,
        "Nome": nome,
        "CPF": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
        "CRM": crm
    }

def medicos_iniciais():#Função que irá gerar 10 médicos fictícios iniciais
    for _ in range(10):
        medicos.append(gerar_dados_medico())

def adicionar_medico():#Função para adicionar um médico manualmente
    nome = input("Digite o nome do médico: ")
    cpf = input("Digite o CPF do médico (somente números): ")
    estado = input("Digite a sigla do estado (ex: SP, RJ): ").upper()
    crm = input("Digite o número do CRM do médico (somente números): ")
    id_medico = gerar_id_medico()

    medico = {
        "ID": id_medico,
        "Nome": nome,
        "CPF": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
        "CRM": f"CRM-{estado}-{crm}"
    }

    medicos.append(medico)
    print(f"Médico {nome} adicionado com sucesso!")

def excluir_medico():# função para excluir um médico pelo ID deste.
    id_medico = input("Digite o ID do médico a ser excluído: ")
    global medicos
    medicos = [medico for medico in medicos if medico["ID"] != id_medico]
    print(f"Médico com ID {id_medico} excluído com sucesso!")

def listar_medicos():#função para listar todos os médicos
    if not medicos:
        print("Não há médicos cadastrados.")
    else:
        for medico in medicos:
            print(f"ID: {medico['ID']}, Nome: {medico['Nome']}, CPF: {medico['CPF']}, CRM: {medico['CRM']}")

medicos_iniciais()#médicos iniciais

# Exemplo de menu para o usuário
def menu():
    while True:
        print("\n1. Listar médicos")
        print("2. Adicionar médico")
        print("3. Excluir médico")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_medicos()
        elif escolha == "2":
            adicionar_medico()
        elif escolha == "3":
            excluir_medico()
        elif escolha == "4":
            break
        else:
            print("Opção inválida!")

# Executar o menu
menu()

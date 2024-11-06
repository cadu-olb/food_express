import os
import time

# Dados iniciais de restaurantes
restaurantes = [
    {"nome": "Mamamia", "cozinha": "Pizzaria", "ativo": False},
    {"nome": "Tostadin", "cozinha": "Churrascaria", "ativo": True},
    {"nome": "JaponFood", "cozinha": "Japonês", "ativo": False}
]

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def voltar_ao_menu():
    input("\nPressione Enter para voltar ao menu principal.")

def cadastrar_restaurante():
    limpar_console()
    print("Cadastro de Restaurante")
    
    # Solicita o nome e verifica duplicidade antes de pedir o tipo de cozinha
    nome_restaurante = input("Digite o nome do seu restaurante: ").strip()
    if any(r["nome"].lower() == nome_restaurante.lower() for r in restaurantes):
        print("Erro: Já existe um restaurante com esse nome.")
        voltar_ao_menu()
        return  # Sai da função se o nome já estiver cadastrado

    # Solicita o tipo de cozinha somente se o nome for único
    tipo_cozinha = input("Qual é o tipo de cozinha do restaurante? ").strip()
    if nome_restaurante and tipo_cozinha:
        restaurantes.append({"nome": nome_restaurante, "cozinha": tipo_cozinha, "ativo": False})
        print(f"Restaurante '{nome_restaurante}' de cozinha '{tipo_cozinha}' cadastrado com sucesso.")
    else:
        print("Erro: Nome do restaurante e tipo de cozinha não podem estar vazios.")
    
    voltar_ao_menu()

def listar_restaurantes():
    limpar_console()
    print("Lista de Restaurantes Ativos:\n")
    ativos = [restaurante for restaurante in restaurantes if restaurante["ativo"]]

    if ativos:
        for i, restaurante in enumerate(ativos, 1):
            print(f"{i}. {restaurante['nome']} - Cozinha: {restaurante['cozinha']}")
    else:
        print("Nenhum restaurante ativo cadastrado.")

    voltar_ao_menu()

def ativar_restaurante():
    limpar_console()
    print("Ativação de Restaurante")
    nome_restaurante = input("Digite o nome do seu restaurante: ").strip()

    for restaurante in restaurantes:
        if restaurante["nome"].lower() == nome_restaurante.lower():
            if not restaurante["ativo"]:
                restaurante["ativo"] = True
                print(f"Restaurante '{nome_restaurante}' ativado com sucesso.")
            else:
                print(f"Restaurante '{nome_restaurante}' já está ativo.")
            break
    else:
        print("Restaurante não encontrado. Cadastre-o antes de ativar.")

    voltar_ao_menu()

def excluir_restaurante():
    limpar_console()
    print("Exclusão de Restaurante")

    while True:
        nome_restaurante = input("Digite o nome do restaurante que deseja excluir: ").strip()

        for i, restaurante in enumerate(restaurantes):
            if restaurante["nome"].lower() == nome_restaurante.lower():
                del restaurantes[i]  # Remove o restaurante pelo índice
                print(f"Restaurante '{nome_restaurante}' excluído com sucesso.")
                voltar_ao_menu()  # Aguarda o usuário antes de retornar ao menu
                return  # Sai da função após excluir
        else:
            print("Restaurante não encontrado.")
            opcao = input("Deseja tentar novamente? (S)im ou (M)enu principal: ").strip().lower()
            if opcao == "m":
                break


    voltar_ao_menu()

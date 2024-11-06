import time
from funcoes import (limpar_console, voltar_ao_menu, cadastrar_restaurante, 
                     listar_restaurantes, ativar_restaurante, excluir_restaurante)

def menu_principal():
    while True:
        limpar_console()
        print("\n** 𝑓𝑜𝑜𝑑 𝑒𝑥𝑝𝑟𝑒𝑠𝑠 **\n")
        print("1. Cadastrar restaurante")
        print("2. Listar restaurantes ativos")
        print("3. Ativar restaurante")
        print("4. Excluir restaurante")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ").strip().lower()

        if opcao == "1":
            cadastrar_restaurante()
        elif opcao == "2":
            listar_restaurantes()
        elif opcao == "3":
            ativar_restaurante()
        elif opcao == "4":
            excluir_restaurante()
        elif opcao == "5" or opcao == "sair":
            print("\nObrigado por usar o Food Express!")
            time.sleep(1)
            break  # Sai do loop principal e encerra o programa
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)  # Pausa para o usuário ler a mensagem antes de limpar

# Executa o programa chamando o menu principal
if __name__ == "__main__":
    menu_principal()


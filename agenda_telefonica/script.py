from my_lib_agenda_telefonica import *

while True:
    print("----------------------------------------------------------------")
    print("Agenda telefonica")
    print("\n[1] - Adicionar contato")
    print("[2] - Lista de contatos")
    print("[3] - Editar contato")
    print("[4] - Marcar/desmarcar contato como favorito")
    print("[5] - Deletar contato")
    print("[6] - Sair")

    r = input("\nQual opção deseja realizar? ")
    while int(r) not in range(1,7):
        print("\nOpção inválida. Tente novamente")
        r = input("Qual opção deseja realizar? ")

    if r == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(lista_contatos, nome, telefone, email)

    elif r == "2":
        listar_contatos(lista_contatos)

    elif r == "3":
        listar_contatos(lista_contatos)
        contato_selecionado = input("Digite o número do contato que deseja editar: ")
        while int(contato_selecionado) - 1 not in range(len(lista_contatos)):
            contato_selecionado = input("Digite o número do contato que deseja editar: ")
        novo_nome =  input(f"Novo nome para o contato (0 caso deseje manter o mesmo nome) {contato_selecionado}: ")
        novo_telefone = input(f"Novo telefone para o contato (0 caso deseje manter o mesmo telefone) {contato_selecionado}: ")
        novo_email = input(f"Novo email para o contato (0 caso deseje manter o mesmo email) {contato_selecionado}: ")
        editar_contato(lista_contatos, contato_selecionado, novo_nome, novo_telefone, novo_email)

    elif r == "4":
        listar_contatos(lista_contatos)
        contato_selecionado = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
        while int(contato_selecionado) - 1 not in range(len(lista_contatos)):
            contato_selecionado = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
        marca_desmarca_favorito(lista_contatos, contato_selecionado)
    
    elif r == "5":
        listar_contatos(lista_contatos)
        contato_selecionado = input("Digite o número do contato que deseja deletar: ")
        while int(contato_selecionado) - 1 not in range(len(lista_contatos)):
            contato_selecionado = input("Digite o número do contato que deseja deletar: ")
        deletar_contato(lista_contatos, contato_selecionado)

    elif r == "6":
        exit()
    
    
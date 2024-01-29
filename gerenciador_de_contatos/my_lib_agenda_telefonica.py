lista_contatos = []

def adicionar_contato(lista_contatos, nome, telefone, email):
    dicionario_contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    lista_contatos.append(dicionario_contato)
    print("Contato adcionado con sucesso")
    return

def listar_contatos(lista_contatos):
    for index,contato in enumerate(lista_contatos, start=1):
        fav_check = "★" if contato["favorito"] else " "
        print(f"{index}. [{fav_check}] - Nome: {contato["nome"]}, Telefone: {contato["telefone"]}, Email: {contato["email"]}")
    return

def editar_contato(lista_contatos, contato_selecionado, novo_nome_contato, novo_telefone, novo_email):
    contato = lista_contatos[int(contato_selecionado) - 1]
    contato["nome"] = novo_nome_contato
    contato["telefone"] = novo_telefone
    contato["email"] = novo_email
    print("Contato editado com sucesso")
    return

def marca_desmarca_favorito(lista_contatos, contato_selecionado):
    contato = lista_contatos[int(contato_selecionado) - 1]
    contato["favorito"] = not contato["favorito"]
    marcacao = "marcado" if contato["favorito"] == True else "desmarcado"
    print(f"Contato {marcacao} como favorito com sucesso")

def deletar_contato(lista_contatos, contato_selecionado):
    lista_contatos.pop(int(contato_selecionado) - 1)
    return
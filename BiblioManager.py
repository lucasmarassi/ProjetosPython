from pymongo.mongo_client import MongoClient
from prettytable import PrettyTable

client = MongoClient("mongodb+srv://projetoBruno:123@cluster0.qcgmm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client['projetoBruno3']
collection = db['livros']
collection2 = db['usuario']
collection3 = db['emprestimo']
collection4 = db['devolucao']

try:


    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

grid_livro = PrettyTable(['TITULO', 'AUTOR', 'ISBN', 'CATEGORIA'])
grid_usuario = PrettyTable(['NOME', 'MATRICULA', 'CURSO'])
grid_emprestimo = PrettyTable(['ISBN_LIVRO', 'MATRICULA', 'DATA_EMPRESTIMO', 'DATA_DEVOLUCAO', 'DEVOLVIDO'])
grid_devolucao = PrettyTable(['ISBN_LIVRO', 'MATRICULA', 'DATA_DEVOLUCAO', 'DEVOLVIDO'])
def Create_livro():
    titulo = input("Digite o título: ")
    autor = input("Digite o autor: ")
    isbn = input("Digite o ISBN: ")
    categoria = input("Digite a categoria: ")

    # Continua pedindo os dados até que nenhum deles seja uma string vazia ou um único espaço
    while titulo == " " or autor == " " or isbn == " " or categoria == " " or titulo == "" or autor == "" or isbn == "" or categoria == "":
        print("Digite as informações corretamente!")
        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")
        isbn = input("Digite o ISBN: ")
        categoria = input("Digite a categoria: ")

    cadastro_livros = {
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "categoria": categoria
    }

    # Insere o livro na coleção (certifique-se de que collection está definido)



    # Verifica se já existe um livro com o mesmo ISBN
    verificacao = collection.find_one({"isbn": isbn})

    if verificacao:
        print("ISBN já existente.")
    else:
        collection.insert_one(cadastro_livros)
        print("Documento inserido com sucesso!")


def Read_livro():
    resp = "s"  # Inicializa a variável de controle do loop
    
    while resp == "s":
        titulo = input("Digite o nome livro que deseja visualizar as informações: ")
        consulta = {"titulo": titulo}
        
        documentos = list(collection.find(consulta))  # Converte o cursor em uma lista
        
        if not documentos:
            print("Documentos não encontrados.")
        else:
            print("Documentos encontrados:")
            for doc in documentos:
                grid_livro.add_row([doc['titulo'], doc['autor'], doc['isbn'], doc['categoria']])
                print(grid_livro)
        
        resp = input("Deseja continuar com o read? s/n ")  # Atualiza a variável de controle do loop


from bson import ObjectId  # Importar se o ID for do tipo ObjectId


def Update_livro():
    consulta = input("Digite o isbn do livro que você quer acessar: ")
    campo = input("Digite o campo que você quer modificar: ")
    valor = input("Digite o novo valor: ")

    # Converte a string 'consulta' para ObjectId, se o '_id' no MongoDB for do tipo ObjectId
    consulta = {"isbn": consulta}

    # Atualiza o campo com o novo valor
    novo_valor = {"$set": {campo: valor}}

    collection.update_one(consulta, novo_valor)
    print("Livro atualizado com sucesso.")


def Delete_livro():

    criterio = input("Digite o isbn do livro que deseja remover: ")
    consulta = {"isbn":criterio}

    resultado_delete = collection.delete_one(consulta)
    if resultado_delete.deleted_count > 0:
        print("Documento removido com sucesso!")
    else:
           print("Nenhum documento encontrado para remover.")




def Create_usuario():
    nome = input("Digite o nome: ")
    matricula = input("Digite o matricula: ")
    curso = input("Digite o curso: ")


    # Continua pedindo os dados até que nenhum deles seja uma string vazia ou um único espaço
    while nome == " " or matricula == " " or curso == " " or nome == "" or matricula == "" or curso == "" :
        print("Digite as informações corretamente!")
        nome = input("Digite o nome: ")
        matricula = input("Digite o matricula: ")
        curso = input("Digite o curso: ")

    cadastro_usuarios = {
        "nome": nome,
        "matricula": matricula,
        "curso": curso

    }

    # Insere o livro na coleção (certifique-se de que collection está definido)

    # Verifica se já existe um livro com o mesmo matricula
    verificacao = collection2.find_one({"matricula": matricula})

    if verificacao:
        print("matricula já existente.")
    else:
        collection2.insert_one(cadastro_usuarios)
        print("Documento inserido com sucesso!")


def Read_usuario():
    resp = "s"  # Inicializa a variável de controle do loop

    while resp == "s":
        nome = input("Digite o nome usuario que deseja visualizar as informações: ")
        consulta = {"nome": nome}

        documentos = list(collection2.find(consulta))  # Converte o cursor em uma lista

        if not documentos:
            print("Documentos não encontrados.")
        else:
            print("Documentos encontrados:")
            for doc in documentos:

                grid_usuario.add_row([doc['nome'], doc['matricula'], doc['curso']])
                print(grid_usuario)

        resp = input("Deseja continuar com o read? s/n ")  # Atualiza a variável de controle do loop





def Update_usuario():
    consulta = input("Digite o matricula do usuario que você quer acessar: ")
    campo = input("Digite o campo que você quer modificar: ")
    valor = input("Digite o novo valor: ")
    while consulta == " " or  campo == " " or valor == " " or  consulta == "" or campo == "" or valor == "":
        print("digite valores certos")
        consulta = input("Digite o matricula do usuario que você quer acessar: ")
        campo = input("Digite o campo que você quer modificar: ")
        valor = input("Digite o novo valor: ")

    consulta = {"matricula": consulta}

    # Atualiza o campo com o novo valor
    novo_valor = {"$set": {campo: valor}}
    if campo == "matricula":
        print("nao é possivel modificar a matricula pois é um dado unico de cada usuario.")
    else:

        collection2.update_one(consulta, novo_valor)
        print("usuario atualizado com sucesso.")


def Delete_usuario():
    criterio = input("Digite o matricula do usuario que deseja remover: ")
    consulta = {"matricula": criterio}

    resultado_delete = collection2.delete_one(consulta)
    if resultado_delete.deleted_count > 0:
        print("Documento removido com sucesso!")
    else:
        print("Nenhum documento encontrado para remover.")





from datetime import datetime
def Create_emprestimo():
    isbn = input("Digite o isbn(codigo) do livro: ")
    matricula = input("Digite o matricula: ")



    # Continua pedindo os dados até que nenhum deles seja uma string vazia ou um único espaço
    while isbn == " " or matricula == " "  or isbn == "" or matricula == "" :
        print("Digite as informações corretamente!")
        isbn = input("Digite o isbn(codigo) do livro: ")
        matricula = input("Digite o matricula: ")


    cadastro_emprestimo = {
        "isbn_livro": isbn,  # ID do livro emprestado
        "matricula": matricula,  # ID do usuário que emprestou
        "data_emprestimo": datetime.now(),
        "data_devolucao": None,
        "devolvido": False

    }
    verificacao_matricula=collection2.find_one({"matricula": matricula})

    verificacao = collection.find_one({"isbn": isbn}) # existe na tabela livro
    verificacao3 = collection3.find_one({"isbn_livro": isbn})  # se ja existe o livro na tabela emprestimo
    if verificacao_matricula:
        if verificacao:
            if verificacao3:
                print("livro ja emprestado.")
            else:

                collection3.insert_one(cadastro_emprestimo)
                print("Documento inserido com sucesso!")





        else:
            print("esse livro nao foi cadastrado")
    else:
        print("esse matricula nao foi cadastrada")
def Read_emprestimo():
    resp = "s"  # Inicializa a variável de controle do loop

    while resp == "s":
        isbn= input("Digite o isbn do livro que deseja visualizar as informações: ")
        consulta = {"isbn_livro": isbn}

        documentos = list(collection3.find(consulta))  # Converte o cursor em uma lista

        if not documentos:
            print("Documentos não encontrados.")
        else:
            print("Documentos encontrados:")
            for doc in documentos:
                grid_emprestimo.add_row([doc['isbn_livro'], doc['matricula'], doc['data_emprestimo'], doc['data_devolucao'], doc['devolvido'] ])
                print(grid_emprestimo)

        resp = input("Deseja continuar com o read? s/n ")  # Atualiza a variável de controle do loop


from bson import ObjectId  # Importar se o ID for do tipo ObjectId


def Delete_emprestimo():
    criterio = input("Digite o isbn do livro que deseja remover: ")
    consulta = {"isbn_livro": criterio}

    # Verifica se o empréstimo existe
    emprestimo = collection3.find_one(consulta)

    if emprestimo:
        devolucoes = collection4.find(consulta)  # Retorna todos os registros de devolução para esse ISBN

        # Itera sobre todas as devoluções para verificar se alguma tem uma data de devolução posterior à data de empréstimo
        devolvido = False
        for devolucao in devolucoes:
            if emprestimo['data_emprestimo'] < devolucao['data_devolucao']:
                devolvido = True
                break

        if devolvido:
            resultado_delete = collection3.delete_one(consulta)
            if resultado_delete.deleted_count > 0:
                print("Documento removido com sucesso!")
            else:
                print("Nenhum documento encontrado para remover.")
        else:
            print("O livro ainda não foi devolvido ou a data de devolução é anterior à data do empréstimo.")
    else:
        print("Empréstimo não encontrado.")


def Create_devolucao():
    isbn = input("Digite o isbn(codigo) do livro: ")
    matricula = input("Digite o matricula: ")



    # Continua pedindo os dados até que nenhum deles seja uma string vazia ou um único espaço
    while isbn == " " or matricula == " "  or isbn == "" or matricula == "" :
        print("Digite as informações corretamente!")
        isbn = input("Digite o isbn(codigo) do livro: ")
        matricula = input("Digite o matricula: ")


    cadastro_devolucao = {
        "isbn_livro": isbn,  # ID do livro emprestado
        "matricula": matricula,  # ID do usuário que emprestou
        "data_devolucao":  datetime.now(),
        "devolvido": True

    }
    verificacao_matricula=collection3.find_one({"matricula": matricula})

    verificacao = collection3.find_one({"isbn_livro": isbn}) # existe o livro na tabela emprestimo

    if verificacao_matricula:
        if verificacao:


                collection4.insert_one(cadastro_devolucao)
                print("Documento inserido com sucesso!")





        else:
            print("esse livro nao foi cadastrado na tabela emprestimos")
    else:
        print("esse matricula nao foi cadastrada na tabela emprestimos")


def Read_devolucao():
    resp = "s"  # Inicializa a variável de controle do loop

    while resp == "s":
        isbn= input("Digite o isbn do livro que deseja visualizar as informações: ")
        consulta = {"isbn_livro": isbn}

        documentos = list(collection4.find(consulta))  # Converte o cursor em uma lista

        if not documentos:
            print("Documentos não encontrados.")
        else:
            print("Documentos encontrados:")
            for doc in documentos:
                grid_devolucao.add_row([doc['isbn_livro'], doc['matricula'], doc['data_devolucao'],doc['devolvido']])
                print(grid_devolucao)

        resp = input("Deseja continuar com o read? s/n ")  # Atualiza a variável de controle do loop


from bson import ObjectId  # Importar se o ID for do tipo ObjectId










resp1 = "s"  # Inicializa a variável de controle do loop

while resp1 == "s":
    tabela=input("digite a tabela q vc quer acessar: 1-livros, 2-usuario, 3-Gerenciamento de emprestimos, 4-Gerenciamento de devolucoes :")
    while tabela == " "  or tabela == "" :
        print("digite corretamente os valores")
        tabela = input("digite a tabela q vc quer acessar: 1-livros, 2-usuario, 3-Gerenciamento de emprestimos, 4-Gerenciamento de devolucoes:")


    if tabela== "1" :
        campo = input("digite os recursos q vc quer acessar de livros: 1-cadastrar, 2-read, 3-update, 4-delete:")
        while campo == " " or campo == "":
            print("digite corretamente os valores")
            campo = input("digite os recursos q vc quer acessar de livros: 1-cadastrar, 2-read, 3-update, 4-delete:")

        if campo == "1":
            Create_livro()
        elif campo == "2":
            Read_livro()
        elif campo == "3":
            Update_livro()
        elif campo == "4":
            Delete_livro()

    if tabela == "2":
        campo = input("digite os recursos q vc quer acessar de usuarios: 1-cadastrar, 2-read, 3-update, 4-delete:")
        while campo == " " or campo == "":
            print("digite corretamente os valores")
            campo = input("digite os recursos q vc quer acessar de usuarios: 1-cadastrar, 2-read, 3-update, 4-delete:")

        if campo == "1":
            Create_usuario()
        elif campo == "2":
            Read_usuario()
        elif campo == "3":
            Update_usuario()
        elif campo == "4":
            Delete_usuario()

    if tabela == "3":
        campo = input("digite os recursos q vc quer acessar de emprestimo: 1-cadastrar, 2-read, 3-delete:")
        while campo == " " or campo == "":
            print("digite corretamente os valores")
            campo = input("digite os recursos q vc quer acessar de emprestimo: 1-cadastrar, 2-read, 3-delete:")

        if campo == "1":
            Create_emprestimo()
        elif campo == "2":
            Read_emprestimo()
        elif campo == "3":
            Delete_emprestimo()



    if tabela == "4":
        campo = input("digite os recursos q vc quer acessar de emprestimo: 1-cadastrar, 2-read:")
        while campo == " " or campo == "":
            print("digite corretamente os valores")
            campo = input("digite os recursos q vc quer acessar de emprestimo: 1-cadastrar, 2-read:")

        if campo == "1":
            Create_devolucao()
        elif campo == "2":
            Read_devolucao()


    resp1 = input("Deseja continuar utilizando o programa? s/n ")
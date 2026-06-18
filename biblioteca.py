def cadastrar_livro(id , nome, autor, editora):
        print('-' * 5, 'Menu Cadastrar Livro', '-' *5)
        dicionario = {}

        dicionario['id'] = int(input(id))
        dicionario['nome']= input(nome)
        dicionario['autor'] = input(autor)
        dicionario['editora'] = input(editora)
        return dicionario


def mostrar_livro(livro):
    print('-' * 15)
    print(f'ID: {livro['id']}')
    print(f'Nome: {livro['nome']}')
    print(f'Autor: {livro['autor']}')
    print(f'Editora: {livro['editora']}')

        
def consultar_livro():
    print('-' * 5, 'Menu Consultar Livro', '-' *5)
    print('Escolha a opção desejada:')
    print('1 - Consultar todos os Livros:')
    print('2 - Consultar por ID:')
    print('3 - Consultar Livro(s) por Autor:')
    print('4 - Retornar')

    while True:
        usuario = int(input())
        if usuario == 1:
            for livro in lista:
                mostrar_livro(livro)
        elif usuario == 2:
            busca_id = int(input('Digite o ID:'))
            for livro in lista:
                if livro['id'] == busca_id:
                    mostrar_livro(livro)
        elif usuario == 3:
           buscar_autor = input('Digite o nome do autor:')
           for livro in lista:
               if livro['autor'] == buscar_autor:
                   mostrar_livro(livro)
        elif usuario == 4:
            break
        else:
            print('Opção inválida! Tente novamente.')
          
def remover_livro():
    print('-' * 5, 'Menu Remover Livro', '-' *5)
    usuario = int(input('Digite o ID do livro a ser removido:'))
    for livro in lista:
        if livro['id'] == usuario:
            lista.remove(livro)
            print('Livro removido')

lista = []

while True:
    print('Bem vindo a Livraria')
    print('-' * 30)
    print('-' * 7, 'Menu Principal', '-' *7)
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Livro')
    print('2 - Consultar Livro(s)')
    print('3 - Remover Livro')
    print('4 - Sair')

    usuario = int(input())
    print('-' * 30)

    if usuario == 1:
        cadastrar = cadastrar_livro('ID do Livro:','Entre com o nome do Livro:', 
                                    'Entre com o autor do Livro:', 'Entre com a editora do livro:')
        lista.append(cadastrar)

    elif usuario == 2:
        consultar_livro()

    elif usuario == 3:
        remover_livro()
    elif usuario == 4:
        break

    else:
        print('Opção inválida.. tente novamente.')
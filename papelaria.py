def validar_escolha(mensagem, opcao):
    while True:
        usuario = input(mensagem)
        if usuario in opcao:
            return usuario
        else:
            print('Escolha inválida, entre com o tipo de serviço novamente...')


def validar_pagina(mensagem, min, max):
    while True:
        usuario = int(input(mensagem))
        if usuario < min:
            print('Não antingiu o minímo necessáio para a compra!')
            continue
        elif usuario > max:
            print('Não aceitamos, tantas páginas de uma vez..')
            continue
        return usuario

dicionario = {'DIG': 1.10, 'ICO': 1.00, 'IPB': 0.40, 'FOT': 0.20}



while True:
    print('Bem vindo a Copiadora')
    print('Entre com a o tipo de serviço desejado:')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')

    escolha =  validar_escolha('DIGITE:', dicionario)

    paginas = validar_pagina('Entre com o número de páginas:', 10 , 20000)

    print('Deseja adicionar mais algum serviço?')
    print('1 - Encardenação Simples - R$15,00')
    print('2 - Encardenação Capa Dura - R40,00')
    print('0 - Não desejo mais nada')

    continuar = int(input(''))

    total = dicionario[escolha] * paginas
    extra = 0


    if continuar == 1 :
        extra = 15
    elif continuar == 2:
        extra = 40
    elif continuar == 0:
        break

    total_final = total + extra

    encerrar = int(input('Deseja mais alguma coisa?'))
    if encerrar == 5:
        break


print(f'Valor total {total}')
print(f'Valor total com o extra: {total_final}')
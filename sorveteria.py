def validar_sabor(pergunta):
    while True:
        usuario = input(pergunta)
        if usuario == 'CP' or usuario == 'AC':
            return usuario
        else:
            print('Sabor inválido! Tente novamente.')
     

        
def validar_tamanho(pergunta):
    while True:
        usuario = input(pergunta)
        if usuario == 'P' or usuario == 'M' or usuario == 'G':
            return usuario    
        else:
            print('Sabor inválido! Tente novamente.')


somador = 0

while True:
    print('-' * 49)
    print(' ' * 10 ,'Bem vindo a sorveteria')
    print(' ' * 15 ,'Cardápio')
    print('-' * 49)
    print('-' * 3 , '|', 'Tamanho', '|', 'Cupuaçu (CP)', '|', 'Açaí (AC)', ' ', '|', '-' * 3)
    print('-' * 3 , '|', ' ' * 2, 'P', ' ' * 2, '|', ' ' * 2,  'R$9,00', ' ' * 2, '|', ' ' , 'R$11,00', ' ', '|', '-' * 3)
    print('-' * 3 , '|', ' ' * 2, 'M', ' ' * 2, '|', ' ' * 2,  'R$14,00', ' ' * 1 , '|' , ' ', 'R$16,00', ' ', '|', '-' * 3)
    print('-' * 3 , '|', ' ' * 2, 'G', ' ' * 2, '|', ' ' * 2,  'R$18,00', ' ' * 1, '|', ' ', 'R$20,00', ' ' , '|', '-' * 3)
    print('-' * 49)

    
    sabor = validar_sabor('Entre com o sabor desejado:')

    tamanho = validar_tamanho('Entre com o tamanho desejado:')

    if sabor == 'CP':
        print(f'Você pediu um Cupuaçu no tamanho {tamanho}')
    elif sabor == 'AC':
        print(f'Você pediu um Açai no tamanho {tamanho} ')
    else:
        print()

    if sabor == 'AC' and tamanho == 'P':
        somador += 11
    elif sabor == 'AC' and tamanho == 'M':
        somador += 16
    elif sabor == 'AC' and tamanho == 'G':
        somador += 20
    elif sabor == 'CP' and tamanho == 'P':
        somador += 9
    elif sabor == 'CP' and tamanho == 'M':
        somador += 14
    elif sabor == 'CP' and tamanho == 'G':
        somador += 18


    continuar = input('\nDeseja mais alguma coisa? S/N')

    if continuar == 'N':
        break
    elif continuar == 'S':
        continue
    else:
        print('Opção inválida!')



print(f'O valor total a ser pago: R${somador}')

    
  





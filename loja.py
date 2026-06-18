print('Seja bem vindo a Loja')

produto = float(input('Entre com o valor do produto:'))
quantidade = int(input('Entre com a quantidade do produto:'))

total = produto * quantidade

if total < 2500:
    print(f'O valor total da sua compra deu: {total}')
elif total >= 2500 and total < 6000:
    desconto = (4/100) * total
    cDesconto = total - desconto
    print(f'O valor total da sua compra deu: {total} \nCom desconto: {cDesconto}')
elif total >= 6000 and total < 10000:
    desconto = (7/100) * total
    cDesconto = total - desconto
    print(f'O valor total da sua compra deu: {total} \nCom desconto: {cDesconto}')
elif total >= 10000:
    desconto = (11/100) * total
    cDesconto = total - desconto
    print(f'O valor total da sua compra deu: {total} \nCom desconto: {cDesconto}')
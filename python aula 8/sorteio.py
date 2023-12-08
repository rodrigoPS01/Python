import random

lista = []

while True:
    acao = int(input('''
            1 - sair
            2 - continuar
            '''))
    if acao == 1:
        break
    elif acao != 2:
        print('deu erro boy')
        continue
    nome = str(input('Qual o nome do cliente: '))
    cpf = int(input('Qual o cpf do cliente: '))
    valor_compra = float(input('Qual o valor da compra: '))
    dicionario_cliente = {
        "Nome": nome,
        "Cpf": cpf,
        "Valor": valor_compra
    }
    lista.append(dicionario_cliente)
    


print(f'Parabens {random.choice(lista)} você foi o escolhido')
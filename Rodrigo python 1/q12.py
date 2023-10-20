controle = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Qual o preço do produto: '))
    controle = controle + preço

    if produto == ('acabar'):
        break

print(f'O valor total da compra é de R${controle}')
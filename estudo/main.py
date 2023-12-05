from funções import *
numeros = []
while True:
    n1 = int(input('Qual número você gostaria de adicionar: '))
    continuar = str(input('Você gostadia de adicionar mais um número? '))
    if continuar == 'Não' or continuar == 'n':
        break
    numeros.append(n1)

print(f'A média dos números que você escreveu é {media_numerica(numeros)}')
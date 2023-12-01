from escola.matematica import *

numeros = []

while True:
    n1 = float(input('Qual número você gostaria de analisar: '))
    numeros.append(n1)
    continuar = str(input('Ainda possui algum número para adicionar: '))
    if continuar == 's':
        continue
    else:
        break

print(media_numeros(numeros))
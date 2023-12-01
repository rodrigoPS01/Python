def maior_numero(numeros = list):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

def menor_numero(numeros = list):
    menor = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    return menor

def media_numeros(numeros = list):
    media = 0
    for numero in numeros:
        media = media + numero
    return media / len(numeros)
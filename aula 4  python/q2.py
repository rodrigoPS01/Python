def quantia(palavra:str):
    espaço = 0
    quan_letras = 0
    sinais = 0
    quantias = []
    for letra in palavra.lower():
        if letra == '':
            espaço = espaço + 1
        elif letra in 'abcdefghijklmnopqrstuvwxyz':
            quan_letras = quan_letras + 1
        else:
            sinais = sinais + 1
    return quantia[espaço, quan_letras, sinais]

palavra = str(input('Diga uma palavra ou frase: '))

print(quantia(palavra))


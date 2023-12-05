letras = str('abcdefghijklmnopqrstuvwxyz')
resposta = ''
opição = str(input(''' O que você gostaria de fazer:
                    1 = criptografar
                    2 = descriptografar
                    '''))

if opição == '1':
    criptografrar = str(input('Digite o texto que você gostaria de criptografar: ')).lower()
    quantia = int(input('Quantas casas você letras você gostaria de avançar para fazer a criptografia: '))
    for letra in criptografrar:
        if letra == '':
            letra = -1000
        resposta += chr(ord(letra) + quantia)
elif opição == '2':
    criptografrar = str(input('Digite o texto que você gostaria de descriptografar: ')).lower()
    quantia = int(input('Quantas casas você letras você gostaria de avançar para fazer a criptografia: '))
    for letra in criptografrar:
        if letra == '':
            letra = -1000
        resposta += chr(ord(letra) - quantia)        

print(resposta)
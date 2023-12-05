texto = str('Olá mundo')
resultado = ''
for letra in texto:
    resultado += chr(ord(letra) + 1)

print(resultado)
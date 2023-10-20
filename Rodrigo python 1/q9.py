frase = str(input('Digite uma frase qualquer: ')).lower()
vogais = 0

for letra in (frase):
    if letra in ('aeiou'):
        vogais = vogais + 1

print(f'A sua frase tem {vogais} vogais')
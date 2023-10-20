frase = str(input('Digite uma frase qualquer: ')).lower()
vogais = 0
consoantes = 0
for letra in (frase):
    if letra in ('aeiou'):
        vogais = vogais + 1
    elif letra in ('bcdfghjklmnpqrstvwxyz'):
        consoantes = consoantes + 1
print(f'A sua frase tem {vogais} vogais e {consoantes} consoantes')
def imc(peso:float, altura:float):
    peso / (altura**2)

imcs = []

for x in range(4):
    peso = float(input('Qual o seu peso: '))
    altura = float(input('Qual a sua altura: '))
    imcs.append(imc(peso,altura))

print(imcs)
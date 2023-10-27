produtos = [('maça', 2.5), ('Banana', 1.75), ('Laranja', 3.00)]
total = 0

for x in produtos:
    quantia = int(input(f'Quandos {x[0]} você comprou'))
    total = total + (x[1] * quantia)

print(f'Você deve pagar um total de {total} reais')
# nomes = []

# for x in range(5):
#     nome = str(input('Digite um nome: '))
#     nomes.append (nome)

# print(nomes)

nomes = []

while len(nomes) < 5:
    nome = str(input('Digite um nome: '))
    nomes.append (nome)

WhileTrue:
n1 = int(input('Diga qual posição você gostaria de mudar: '))
if n1 > 5 and n1 < 0:
        print('valor não encontrado')
else:
    break


nome = str(input('Diga um nome: '))
nomes.insert(n1 - 1 ,nome)
print(nomes)
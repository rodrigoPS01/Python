cores = {'Amarelo', 'Azul', 'Vermelho', 'Verde'}
cores2 = []

while True:
    nome = str(input('Digite uma cor: '))
    if nome == 'sair':
        break
    cores2.append(nome)

cores.update(cores2)

print(cores)


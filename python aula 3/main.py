alunos = []
maior = []
melhor = []
while True:
    nome = str(input('Diga o nome do aluno: '))
    if nome == ('fim'):
        break
    nota = float(input('Diga a nota do aluno: '))
    alunos.append([nome,nota])


for x in alunos:
    if x[1] >= maior:
        maior.append (x[1])
        melhor.append (x[0])

print(f'O melhor aluno é {melhor} e sua nota foi {maior}')


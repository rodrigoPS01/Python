alunos = []
maior = 0
aluno = ''
for x in range(3):
    aluno = str(input('Diga seu nome: '))
    nota = float(input('Digite sua nota: '))
    alunos.append([aluno,nota])


for x in alunos:
    if x[1] > maior:
        maior = x[1]
        aluno = x[0]

print(f'O aluno com maior nota é {aluno} com nota = {maior}')

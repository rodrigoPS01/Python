alunos = []
while True:
    menu = int(input('''
                    1 - Cadastrar aluno
                    2 - Visualizar alunos cadastrados
                    3 - Deletar o aluno
                    0 - Sair
                    '''))

    if menu == 1:
        nome = str(input('Digite o nome do aluno: '))
        cpf = int(input('Qual o CPF do aluno: '))
        turma = str(input('Qual a turma do aluno: '))
        n1 = float(input('Qual a 1° nota do aluno: '))
        n2 = float(input('Qual a 2° nota do aluno: '))
        n3 = float(input('Qual a 3° nota do aluno: '))
        n4 = float(input('Qual a 4° nota do aluno: '))
        pessoa = {
            'nome': (nome),
            'cpf': (cpf),
            'turma': (turma),
            'nota 1': (n1),
            'nota 2': (n2),
            'nota 3': (n3),
            'nota 4': (n4)
        }
        alunos.append(pessoa)
    elif menu == 2:
        print(f'{
            nome = alunos[nome],
            cpf = alunos[cpf]
            turma = alunos[turma]
            nota1 = alunos[n1]
            nota2 = alunos[n2]
            nota3 = alunos[n3]
            nota4 = alunos[n4]}')

    elif menu == 3:
        deletar = str(input('Qual o nome do aluno que você gostaria de deletar: '))
        posição = alunos.index(deletar)
        alunos.pop (posição)

    elif menu == 0:
        break

    elif menu != '0123':
        print('valor invalido')
        continue
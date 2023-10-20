n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

operação = str(input('Qual operação você deseja realizar: '))
resultado = 0
if operação == 'adição' or operação == '+':
    resultado = n1 + n2
elif operação == 'subtração' or operação == '-':
    resultado = n1 - n2
elif operação == 'multiplicação' or operação == '*':
    resultado = n1 * n2
elif operação == 'divição' or operação == '/':
    resultado = n1 / n2
else:
    print('Escreva uma operação valida')

if resultado > 0:
    print('seu resultado é possitivo')
elif resultado < 0:
    print('Seu resultado é negativo')
else:
    print('Seu resultado é 0')

if resultado % 2 == 0:
    print('Seu número é par')
elif resultado % 2 != 0:
    print('Seu número é ímpar')
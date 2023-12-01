from operaçoes import *

escolha = str(input('Qual operação você gostaria de fazer? ' )).lower()
n1 = float(input('Qual o primeiro número: '))
n2 = float(input('Qaual o segundo número: '))

if escolha == 'soma' or escolha == '+' or escolha == 'adição':
    print(f'O resultado da soma é {soma(n1,n2)}')

elif escolha == 'diminuir' or escolha == 'subtrair' or escolha == '-':
    print(f'O resultado da sua subtração é {subtrair(n1,n2)}')

elif escolha == 'multiplicação' or escolha == 'x' or escolha == '*':
    print(f'O resultado da sua multiplicação é {multiplicar(n1,n2)}')
    
elif escolha == 'dividir' or escolha == '/':
    print(f'O resultado da sua divisão é {dividir(n1,n2)}')

else:
    print('A operação escolhida não existe ou foi escrita incorretamente')


# while True:
#     menu = int(input("""
#     Selecione uma operação:
#     1 - Somar
#     2 - Subtrair
#     3 - Multiplicar
#     4 - Dividir
#     0 - Sair
# """))
#     match menu:
#         case 1:
#             print(somar(numero1, numero2))
#         case 2:
#             print(subtrair(numero1, numero2))
#         case 3:
#             print(multiplicar(numero1, numero2))
#         case 4:
#             print(dividir(numero1, numero2))
#         case 0:
#             print("Fim do programa")
#             break
#         case _:
#             print("Opção Inválida")
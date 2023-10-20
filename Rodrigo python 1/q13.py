senha = str(input('Digite sua senha: '))

if len(senha) > 8 and len(senha) < 12:
    print('senha valida')
else:
    print('senha invalida')
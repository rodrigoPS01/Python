sexo = str(input('Diga qual o seu sexo [F|M]: '))

if sexo in ('Ff'):
    print('Você é do sexo feminino')
elif sexo in ('Mm'):
    print('Você é do sexo masculino')
else:
    print('sexo invalido')
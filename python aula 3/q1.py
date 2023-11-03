pessoa = ['abel', 28 , 1.79, True, 35]

pessoa_dicionario = {
    'nome' : 'abel', 'idade' : 28, 'altura' : 1.79, 
    'acidentado' : True, 'milhoes_na_conta' : 35}

list(pessoa_dicionario)
for x in pessoa_dicionario:
    print(x)
print(f'o Dicionario possui {len(pessoa_dicionario)} topicos')
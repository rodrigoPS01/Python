def maior(n1:int, n2:int):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return 'Os números são iguais'

n1 = int(input('Diga um número: '))
n2 = int(input('Diga um número: '))
print(maior(n1,n2))
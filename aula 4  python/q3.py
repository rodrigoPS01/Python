def valor_das_horas(salario:int,horas:int):
    valor = salario / horas
    return valor

salario = int(input('Qual o seu salario: '))
horas = int(input('Quantas horas você trabalha: '))

print(f'Você recebe {valor_das_horas(salario, horas):.2} por hora')
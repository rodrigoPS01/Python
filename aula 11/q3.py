class Empresa:
    def __init__(self) -> None:
        self.lista_de_funcionarios = []

class Funcionario:
    def __init__(self,nome , cargo, salario) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = salario



def add(self):
    nome = input('Qual o nome do funcionario: ')
    cargo = input('Qual o cargo do funcionario: ')
    salario = float(input('Qual o salario do funcionario: '))
    funcionario = Funcionario(nome=nome, cargo=cargo, salario=salario)
    
    self.lista_de_funcionarios.append(funcionario)    



def remv(self):
    nome = input('Digite o nome do funcionario que você gostaria de remover: ')
    for funcionario in self.lista_de_funcionario:
        if funcionario.nome == nome:
            self.funcionarios.remove(nome)


def visualizar():
    print(f'''
    Nome: {Funcionario.nome}
    Cargo: {Funcionario.cargo}
    Salario: {Funcionario.salario}
    ''')



while True:

    menu = int(input('''
    Qual ação você gostaria de fazer
    1 - adicionar funcionario
    2 - remover funcionario
    3 - visualizar funcionarios
    4 - sair
    '''))

    match menu:
        case 1:
            add()
            print('funcionario adicionado')
        case 2:
            remv()
            print('Funcionario removido')
        case 3:
            visualizar()
        case 4:
            break
        case _:
            print('Opção invalida')

class Pessoa:
    def __init__(self, nome:str, idade:int, altura:float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def ver_info(self):
        return f'''
        Informação da Pessoa:
        Nome: {self.nome}
        Idade: {self.idade}
        Altura: {self.altura}
        '''

pessoa1 = Pessoa(nome='Bruno', idade=23, altura=1.72)

#print(pessoa1.ver_info())
pessoa1.__idade = 90
print(pessoa1.__idade)
#print(pessoa1.ver_info())
class Gato:
    def __init__(self, nome:str ,raça:str, peso:float, idade:int, castrado:bool) -> None:
        self.nome = nome
        self.raça = raça
        self.peso = peso
        self.idade = idade
        self.castrado = castrado

def miar(self):
    return f'O {self.nome} miou, dê atenção ao bixo'


gato1 = Gato(nome='chanin', raça='siamês', peso=5.5, idade=5, castrado=False)

gato2 = Gato(nome='polo', raça='sphynx', peso=8.9, idade=3, castrado=True)

miar(gato1)
miar(gato2)
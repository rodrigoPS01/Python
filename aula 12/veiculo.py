class Veiculo:
    def __init__(self, marca:str, modelo:str, ano:int, cor:str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        return f'O veículo {self.modelo} ligou'

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, qtde_portas:str) -> None:
        super().__init__(marca, modelo, ano, cor)
        self.qtde_portas = qtde_portas
    
    def cavalo_de_pau(self):
        return f'O carro {self.modelo} que tem {self.qtde_portas} de portas, fez um cavalo de pau'

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas:int) -> None:
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas

    def empinar(self):
        return f'A moto {self.modelo} de {self.cilindradas} cilindradas está empinando'

carro1 = Carro(marca='BMW', modelo='M4', ano=2020, cor='Azul', qtde_portas=4)

moto1 = Moto(marca='Honda', modelo='Fazer',ano=2022, cor='Branca', cilindradas=250)


print(carro1.ligar())
print(carro1.cavalo_de_pau())

print(moto1.ligar())
print(moto1.empinar())
class Moto:
    def __init__(self, marca:str, modelo:str, cilindradas:int, cor:str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cilindradas = cilindradas
        self.cor = cor

    def buzinar(self):
        return f'A {self.marca} {self.modelo} está buzinando'
    
    def info(self):
        return f'''
        marca: {self.marca}
        modelo: {self.modelo}
        cilindradas: {self.cilindradas}
        cor: {self.cor}
        '''

moto1 = Moto(marca='Honda', modelo='Titan', cilindradas=160, cor='vermelha')
moto2 = Moto(marca='Honda', modelo='Twister', cilindradas=250, cor='Preta')
moto3 = Moto(marca='Honda', modelo='start', cilindradas=150, cor='Prata')

print(moto1.info())
print(moto2.info())
print(moto3.info())








# print(f'A marca da 1° moto é {moto1.marca} ')
# print(f'A cilindrada e a cor da 2° moto é {moto2.cilindradas} e {moto2.cor}')
# print(f'As especificações da 3° moto é {moto3.marca}, {moto3.modelo}, {moto3.cilindradas} e {moto3.cor}')
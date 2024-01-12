class Tamagotchi:
    def __init__(self, nome:str, especie, energia) -> None:
        self.nome = nome
        self.especie = especie
        self.energia = energia

    def brincar(self):
        self.energia -= 5
        if self.energia <= 0:
            print('Seu tamagotchi morreu') 
        return self.energia
    
    def comer(self):
        self.energia += 5
        if self.energia > 100:
            self.energia = 100
        return self.energia
    

tamagotchi1 = Tamagotchi(nome='Chico', especie='Voador', energia=100)

while True:
    menu = int(input('''
    O que você gostaria de fazer
    1 - Brincar
    2 - Comer
    0 - Sair
    '''))

    match menu:
        case 1:
            tamagotchi1.brincar()
        case 2:
            tamagotchi1.comer()
        case 0:
            break
        case _:
            print('Opição invalida')
    
    print(f'Sua energica atual é {tamagotchi1.energia}')
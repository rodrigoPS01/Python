animal = {"Especie": "Cachorro", "Raça": "Pinscher",
           "Idade": int(input('Qual a idade do cachorro: ')), "Adestrado": "Sim"}


if animal['Idade'] > 2:
    animal['Vacinado'] = True
else:
    animal ['Adestrado'] = 'Não'

print(animal)
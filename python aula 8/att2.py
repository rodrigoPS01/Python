
choice = int(input('''O que gostaria de fazer
                   1 - adicionar
                   2 - remover
                   3 - atualizar
                    '''))


if choice == 1:
    nome = str(input('Qual o nome do produto que voccê gostaria de adicionar: '))
    preço = float(input('Qual o seu preço: '))
    quantia = int(input('Qual a quantia desse produto no estoque: '))
    produtos = {
        'nome': nome,
        'preço': preço,
        'quantia': quantia
    }
elif choice == 2:
    nome = str(input('Qual o nome do produto que você gostaria de remover: '))
    posição = 

    produtos['nome'].pop(posição)
    produtos['preço'].pop(posição)
    produtos['quantia'].pop(posição)
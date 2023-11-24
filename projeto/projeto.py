import random
print('lets play a game')
nome = str(input('Qual o seu nome: '))
def vitoria(escolha_do_jogador,escolha_da_ia):

    if escolha_do_jogador == escolha_da_ia:
         return print(f'você jogou {escolha_do_jogador} e a ia jogou {escolha_da_ia} então, deu empate')
    elif escolha_do_jogador == 'pedra' and escolha_da_ia == 'papel' or escolha_do_jogador == 'papel' and escolha_da_ia == 'tesoura' or escolha_do_jogador == 'tesoura' and escolha_da_ia == 'pedra':
        return print(f'{nome}, você jogou {escolha_do_jogador} e a ia {escolha_da_ia} então, você perdeu ;-;')
    else:
         return print(f'Parabens {nome} você jogou {escolha_do_jogador} e a ia {escolha_da_ia} então, você ganhou!!')
    
def analise(escolha_do_usuario, escolha_da_ia):
    if escolha_do_usuario not in ('pedra','papel','tesoura'):
        return 'Jogada invalida ;-;'
    else:
        return ('')
    
while True:
    jogadas = ['Pedra', 'Papel', 'Tesoura']
    jogada = str(input('Qaul jogada você gostaria de fazer: ')).lower()
    jogada_ia = random.choice(jogadas).lower()

    jogada_analisada = analise(jogada,jogada_ia)
    if jogada_analisada == "Jogada invalida ;-;":
        print(jogada_analisada)
        break
    
    vitoria(jogada,jogada_ia)
    break
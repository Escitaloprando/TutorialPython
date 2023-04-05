#Crie um programa que faça o computador jogar Pedra, Papel e Tesoura com você.

import random
inputJogador = int(input('Vamos jogar Pedra, Papel e Tesoura! \n [0] PEDRA \n [1] PAPEL \n [2] TESOURA \n Sua jogada: '))
# pedra(0) > tesoura(2) > papel(1) > pedra(0)
jogadas = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(jogadas) # Seleciona aleatoriamente um item na lista 'jogadas'
jogador = jogadas[inputJogador]# Lê o input númerico do jogador e usa para selecionar o item correspondente na lista
# Computador vence:
if computador == jogadas[0] and jogador == jogadas[2]:
    print('ERA DAS MÁQUINAS! O Computador venceu. \n Computador: {} \n Jogador: {} \n Tente novamente'.format(computador, jogador))
elif computador == jogadas[2] and jogador == jogadas[1]:
    print('ERA DAS MÁQUINAS! O Computador venceu. \n Computador: {} \n Jogador: {} \n Tente novamente'.format(computador, jogador))
elif computador == jogadas[1] and jogador == jogadas[0]:
    print('ERA DAS MÁQUINAS! O Computador venceu. \n Computador: {} \n Jogador: {} \n Tente novamente'.format(computador, jogador))
# Jogador Vence:
elif computador == jogadas[2] and jogador == jogadas[0]:
    print('Viva a humanidade! Você venceu. \n Computador: {} \n Jogador: {} \n Tente novamente'.format(computador, jogador))
elif computador == jogadas[1] and jogador == jogadas[2]:
    print('Viva a humanidade! Você venceu. \n Computador: {} \n Jogador: {} \n Tente novamente'.format(computador, jogador))
elif computador == jogadas[0] and jogador == jogadas[1]:
    print('Viva a humanidade! Você venceu. \n Computador: {} \n Jogador: {} \n Tente novamente'.format(computador, jogador))
# Empate:
else:
    print('Empate! \n Computador: {} \n Jogador: {} \n Tente novamente!'.format(computador, jogador))

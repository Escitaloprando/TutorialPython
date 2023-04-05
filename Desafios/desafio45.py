import random
#Crie um programa que faça o computador jogar Pedra, Papel e Tesoura com você.
jogador = input('Vamos jogar Pedra, Papel e Tesoura! \n [1] PEDRA \n [2] PAPEL \n [3] TESOURA \n Sua jogada: ')
# pedra(1) > tesoura(3) > papel(2) > pedra(1)
jogadas = ['1', '2', '3']
computador = random.choice(jogadas)
# Computador vence:
if (computador == "1" and jogador == "3") or (computador == "3" and jogador == "2") or (computador == "2" and jogador == "1"):
    print('ERA DAS MÁQUINAS! O Computador venceu. \n Computador: {} \n Jogador: {} \n Tente novamente'.format(computador, jogador))
# Jogador Vence:
elif (computador == "3" and jogador == "1") or (computador == "2" and jogador == "3") or (computador == "1" and jogador == "2"):
    print('Viva a humanidade! Você venceu. \n Computador: {} \n Jogador: {} \n Tente novamente'.format(computador, jogador))
# Empate:
else:
    print('Empate! \n Computador: {} \n Jogador: {} \n Tente novamente!'.format(computador, jogador))

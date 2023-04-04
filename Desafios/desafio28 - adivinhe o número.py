# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para que o usuário 
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
#  venceu ou perdeu. 
import random
numeros = [0, 1, 2, 3, 4, 5]
sorteado = int(random.choice(numeros))
tentativa = int(input("Estou pensando em um número de 0 a 5. Qual é? "))
if tentativa == sorteado:
    print('Você acertou! Pensei no número {}'.format(sorteado))
else:
    print('Você errou! Havia pensado no número {}'.format(sorteado))
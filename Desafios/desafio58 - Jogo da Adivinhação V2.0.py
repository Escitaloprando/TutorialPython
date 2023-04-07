# Melhore o jogo do Desafio28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador 
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
chute = []
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorteado = random.choice(numeros)
while chute != sorteado:
    chute = int(input('Tente adivinhar em qual número de 0 a 10 estou pensando! '))
print(f'Parabéns, você acertou! Pensei no número {sorteado}')
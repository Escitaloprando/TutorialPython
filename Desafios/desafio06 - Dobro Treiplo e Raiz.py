#crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada
import math

n=int(input('Digite um número'))
print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {}'.format(n, (n*2), (n*3), (math.isqrt(n))))
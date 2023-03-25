#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.
from math import sin, cos, tan

a=int(input('Digite o ângulo '))
print('O ângulo {:.2f} tem como Seno {:.2f}, Cosseno {:.2f} e Tangente ^{:.2f}'.format(a, sin(a), cos(a), tan(a)))
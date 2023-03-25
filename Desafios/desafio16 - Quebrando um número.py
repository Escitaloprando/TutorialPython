#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua proção inteira.
import math
n=float(input('Digite um número qualquer'))
print('A parte inteira desse número é {}'.format(math.trunc(n)))
#Faça um programa que leia um número qualquer e mostre seu fatorial.
from math import factorial
numero = int(input('Digite um número para saber seu fatorial: '))
contador = numero
print(f'O fatorial de {numero} é: ')
while contador > 0:
    print(f'{contador}', end='') # end='' --> faz com que o print abaixo seja feito na mesma linha
    print(' X ' if contador > 1 else ' = ', end='')
    contador -= 1
print(f'{factorial(numero)}')
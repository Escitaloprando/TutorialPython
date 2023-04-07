#Faça um programa que leia um número qualquer e mostre seu fatorial.
from math import factorial #fatorial de um número
numero = int(input('Digite um número para saber seu fatorial: ')) #recebe o número à ser fatorado
contador = numero #estebelce como contador, o número inserido.
print(f'O fatorial de {numero} é: ')
while contador > 0: #contador sendo o número, se repete até chegar à zero.
    print(f'{contador}', end='') # end='' --> faz com que o print abaixo seja feito na mesma linha
    print(' X ' if contador > 1 else ' = ', end='')
    contador -= 1
print(f'{factorial(numero)}')
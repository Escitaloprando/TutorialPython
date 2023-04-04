# Crie um programa que leia um número inteiro e mostre na tela se ele é paro u impar
numero = int(input('Digite um número '))
if numero % 2 == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} não é par!'.format(numero))
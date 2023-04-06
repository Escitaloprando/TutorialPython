#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
print('Vamos descobrir se um número é primo ou não!')
numero = int(input('Qual número você quer testar? '))
restoDois = int(numero % 2)
restoTres = int(numero % 3)
if restoDois == 0 or restoTres == 0:
    print('O número {} não é um número primo!'.format(numero))
else:
    print('O número {} é um número primo!'.format(numero))
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
import math
n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o segundo número '))
numeros = [n1, n2]
maior = max(numeros)
menor = min(numeros)
if n1 > n2 or n2 > n1:
  print('O número {} é maior do que {}'.format(maior, menor))
else: 
   print('Ambos os números são idênticos!')
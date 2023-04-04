#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Qual é o ano?'))
if ano % 4 == 0:
    print('O ano de {} é um ano bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
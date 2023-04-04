# Desenvolva um programa que pergunte a distãncia de uma viagem em km. Calcule o preço da passagem,
# cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas

distancia = int(input('Quantos quilometros você vai viajar?'))
if distancia <= 200:
    tx = 0.50
    preco = distancia * tx
    print('o custo de sua passagem é de {}'.format(preco))
else:
    tx = 0.45
    preco = distancia * tx
    print('O custo de sua passagem é de {}'.format(preco))
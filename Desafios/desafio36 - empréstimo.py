# Escreva um programa para aprovar empréstimo bancário para a compra de uma casa. O programa vai perguntar o 
# valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
# negado.

salario = float(input('Qual é sua renda total? '))
emprestimo = float(input('Qual é o valor do imóvel? '))
prazo = int(input('Em quantos meses você pretende pagar?'))

parcela = emprestimo / prazo 
if parcela >= salario*0.30:
    print('Seu empréstimo foi negado! A parcela não pode ultrapassar 30% de sua renda')
else:
    print('Seu empréstimo foi aprovado! Serão {} parcelas de R${}'.format(prazo, parcela))
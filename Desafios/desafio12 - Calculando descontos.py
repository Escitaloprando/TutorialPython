#Faça um algortimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p=int(input('Qual é o valor do produto? R$'))
print('Então, com o desconto de 5%, EXCLUSIVO NO EMAIL, vai custar apenas R${:.2f}'.format(p*0.95))
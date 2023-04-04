# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por km acima do limite. 
velocidade = int(input('Qual é sua velocidade? '))
if velocidade > 80:
    print('Acima da velocidade! Você foi multado em R${}'.format(float((velocidade-80)*7)))
else:
    print('Dentro da velocidade permitida. Parabéns!')

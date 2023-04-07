# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
# com a tabela abaixo:
# -Abaixo de 18.5: abaixo do peso
# -Entre 18.5 e 25: peso ideal 
# -25 até 30: sobrepeso 
# 30 até 40: obesidade
# acima de 40: obesidade mórbida.
peso = float(input('Digite seu peso em quilos. '))
altura = float(input('Digite sua altura em metros. '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('Com um IMC de {:.2f}, você está ABAIXO DO PESO'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Com um IMC de {:.2f}, você está no PESO IDEAL'.format(imc))
elif imc >= 25 and imc < 30:
    print('Com um IMC de {:.2f}, você está com SOBREPESO'.format(imc))
elif imc >= 30 and imc < 40:
    print('Com um IMC de {:.2f}, você está com OBESIDADE'.format(imc))
else:
    print('Com um IMC de {:.2f}, você está com OBESIDADE MÓRBIDA'.format(imc))
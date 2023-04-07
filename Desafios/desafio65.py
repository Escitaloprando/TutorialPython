# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e menor valor lido. O programa deve perguntar ao usuário
# se ele quer ou não continuar digitando valores.
soma = 0
entrada = 0
comando = -1
numeros = 0
while comando != 0:
    entrada = int(input('Digite um número inteiro: '))
    numeros += 1
    soma += entrada
    media = soma / numeros
    if numeros == 1:
        print(f'A média do único número digitado é ele mesmo, {entrada}')
    else:
        print(f'A média dos {numeros} numeros digitados é igual à {media}')
    comando = int(input('Você quer digitar mais um número? \n [0] NÃO \n [1] SIM \n COMANDO: '))
    if comando not in [0, 1]:
        print('COMANDO INVÁLIDO! TENTE NOVAMENTE')
        comando = int(input('Você quer digitar mais um número? \n [0] NÃO \n [1] SIM \n COMANDO: '))
print('FIM')
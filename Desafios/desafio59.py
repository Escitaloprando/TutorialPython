# Crie um programa que leia dois valores e mostre um menu na tela;

# [1]somar
# [2]multiplicar
# [3]maior
# [4]novos números
# [5]sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep


opcao = 0
while opcao != 5:
    opcao = 1
    primeiroNumero = int(input('Digite o primeiro número: '))
    segundoNumero = int(input('Digite o segundo número: '))  
    while opcao != 5:
        opcao = int(input('O que você quer fazer com estes número? \n [1] Somar \n [2] Multiplicar \n [3] Maior número \n [4] Novos números \n [5] SAIR \n DIGITE SUA OPÇÃO: '))
        sleep(1)
        if opcao == 1:
            print(f'A soma de {primeiroNumero} com {segundoNumero} é igual à {primeiroNumero+segundoNumero}')
        elif opcao == 2:
            print(f'A multiplicação de {primeiroNumero} por {segundoNumero} é igual à {primeiroNumero*segundoNumero}')
        elif opcao == 3:
            print(f'O maior número entre as opções digitadas é {max(primeiroNumero, segundoNumero)}')   
        elif opcao ==4 :
            opcao = 4  
        else:
            opcao = 5
print('Tchau!')
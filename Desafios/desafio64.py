# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
# a soma entre eles(desconsidere o flag)
soma = 0
numero = 0
entrada = 1
while entrada != 999:
    entrada = int(input(f'Digite o {entrada}° número inteiro! '))
    if entrada != 999:
        soma += entrada
print(f'A soma dos numeros digitados é {soma}')
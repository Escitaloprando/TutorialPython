# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo de alistamento.

# Seu programa também deverá mostrar o tempo que falta ou o que passou do prazo.
ano = int(input('Digite o ano em que você nasceu '))
idade = 2023 - ano
diferença = 18 - idade
if idade < 18:
    print('Você tem {} anos. Se aliste em {} anos'.format(idade, diferença))
elif idade == 18:
    print('Você já tem {} anos. Está na hora de alistar!'.format(idade))
else:
    print('Você tem {} anos. Deveria ter se alistado há {} anos.'.format(idade, diferença*-1))

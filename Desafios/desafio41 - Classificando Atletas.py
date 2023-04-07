# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a sua idade:

# -Até 9 anos: mirim
# -Até 14 anos: infantil
# -Até 19 anos: junior
# -até 21 anos: sênior
# -acima: adulto
ano = int(input('Em que ano você nasceu? '))
idade = 2023 - ano
if idade <= 9:
    print('Por ter {} anos, você faz parte da categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Por ter {} anos, você faz parte da categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Por ter {} anos, você faz parte da categoria JUNIOR'.format(idade))
elif idade <= 21:
    print('Por ter {} anos, você faz parte da categoria SÊNIOR'.format(idade))
else:
    print('Por ter {} anos, você faz parte da categoria ADULTO'.format(idade))
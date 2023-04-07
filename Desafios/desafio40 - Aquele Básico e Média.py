# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de 
# acordo com a média atingida:

# - Média abaixo de 5.0: reprovado
# - Média entre 5.0 e 6.9: recuperação
# - média 7.0 ou superior: aprovado
n1 = float(input('Digite sua primeira nota '))
n2 = float(input('Digite sua segunda nota '))
media = (n1 + n2)/2
if media < 5.0:
    print('Você foi REPROVADO! Skill issue.')
elif media >= 5.0 and media < 6.9:
    print('Você está de RECUPERAÇÃO! Aproveite essa chance.')
else:
    print('Parabéns, você foi APROVADO!')
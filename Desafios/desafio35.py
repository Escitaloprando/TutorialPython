# Desenvolva um programa que leio o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.
r1 = int(input('Digite o comprimento da primeira reta '))
r2 = int(input('Digite o comprimento da segunda reta '))
r3 = int(input('Digite o comprimento da terceira reta '))
if ((r1+r2)>r3) and ((r1+r3)>r2) and ((r2+r3)>r1):
    print('As retas {}, {} e {} formam um triângulo!'.format(r1, r2, r3))
else:
    print('As retas {}, {} e {} não formam um triângulo!'.format(r1, r2, r3))
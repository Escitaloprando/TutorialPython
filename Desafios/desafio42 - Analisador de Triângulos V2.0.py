# Refaço o Desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# -Equilátero: todos os lados iguais
# -Isósceles: dois lados igual
# Escaleno: todos os lados diferentes
r1 = float(input('Digite o valor da primeira reta '))
r2 = float(input('Digite o valor da segunda reta '))
r3 = float(input('Digite o valor da terceira reta '))
if ((r1+r2)>r3) and ((r1+r3)>r2) and ((r2+r3)>r1):
    if r1 == r2 == r3:
        print('As retas {}, {} e {} formam um triângulo EQUILATERO'.format(r1, r2, r3))
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('As retas {}, {} e {} formam um triângulo ISÓSCELES'.format(r1, r2, r3))
    else:
        print('As retas {}, {} e {} formam um triângulo ESCALENO'.format(r1, r2, r3))
else:
    print('As retas {}, {} e {} NÃO formam um triângulo'.format(r1, r2, r3))
#Importação de bibliotecas e módulos

#Importação da biblioteca inteira
import math

n=int(input('Digite um número '))
 #                                     |biblioteca|módulo|                   
print('A raiza quadrada de {} é {}'.format(n, math.sqrt(n)))

#importação do módulo especifico
from math import sqrt
n=int(input('Digite um número '))
#                                            | módulo |
print('A raiza quadrada de {} é {}'.format(n, sqrt(n)))
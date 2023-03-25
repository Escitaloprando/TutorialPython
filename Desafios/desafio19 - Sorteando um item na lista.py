#um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude 
#ele, lendo o nome deles e escrevndo o nome escolhido.

import random

a=input('Digite o nome do primeiro estudante ')
b=input('Digite o nome do segundo estudante ')
c=input('Digite o nome do terceiro estudante ')
d=input('Digite o nome do quarto estudante ')
lista=a ,b , c, d 
print('O estudante escolhido foi o {}'.format(random.choice(lista)))
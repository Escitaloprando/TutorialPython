#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos 
#alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a=input('Digite o nome do primeiro estudante ')
b=input('Digite o nome do segundo estudante ')
c=input('Digite o nome do terceiro estudante ')
d=input('Digite o nome do quarto estudante ')

#minha tentativa:
#lista=a, b, c, d
#print('A ordem de apresentação do primeiro ao último é {}'.format(random.shuffle(lista)))
#ChatGPT:
lista=[a, b, c, d]
random.shuffle(lista)
print('A ordem de apresentação do primeiro ao último é {}'.format(lista))
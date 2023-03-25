#Exemplos de fomatações na função print
#nome=input('Qual é seu nome?')
#print('Feliz em te conhecer {:10}!'.format(nome))
#Feliz em te conhecer Nome      !

#print('Feliz em te conhecer {:-^10}!'.format(nome))
#Feliz em te conhecer ---Nome---!

n1=int(input('Primeiro valor:'))
n2=int(input('Segundo valor:'))
s=n1+n2
m=n1*n2
d=(n1/n2)
di=n1//n2
r=n1%n2
e=n1**n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d), end='')
print(' A divisão inteira é {}, com resto {}'.format(di, r))
#A soma é 6, o produto é 8 e a divisão é 2.000. A divisão inteira é 2, com resto 0

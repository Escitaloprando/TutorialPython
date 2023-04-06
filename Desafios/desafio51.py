# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros 
# termos dessa progressão
# An=A1+(n-1)r
#termo=primeitoTermo+(posicao-1)razao
primeiroTermo = int(input('Insira o primeiro termo de sua progressão aritmética '))
razao = int(input('Ótimo! E qual vai se a razão? '))
print('Uma progressão artimética tem como fórmula An=A1+(n-1)r')
for pa in range(1, 11):
    termo = primeiroTermo+((pa-1)*razao)
    print('A posição {} tem como termo o número {}'.format(pa, termo))
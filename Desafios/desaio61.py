# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da 
# progressão usando a estrutura while.
# An=A1+(n-1)r
#termo=primeitoTermo+(posicao-1)razao
# sourcery skip: move-assign-in-block, while-to-for
primeiroTermo = int(input('Digite o primeiro termo de sua Progressão Artimética: ')) 
razao = int(input('E qual vai ser a razão da PA? '))
n = 0
print(f'Seguem abaixo os dez primeiros termos da PA com Primeiro Termo {primeiroTermo} e razao {razao}: ')
while n < 10:
    n += 1
    termo = primeiroTermo+(n-1)*razao
    print(termo)
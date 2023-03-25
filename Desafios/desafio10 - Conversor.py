#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares elap ode comprar. Considere U$1=R$3,27
n=int(input('Tem quanto aí, patrão? R$'))
#print('Isso vale {:.2f} em dólares americanos'.format(n/3.17))
if n >= 500:
    print('Isso compra U${:.2f}. Coisa ta boa aí, hein!'.format(n/3.17))
else:
    print('Isso compra U${:.2f}. Ta foda né, doidão'.format(n/3.17))
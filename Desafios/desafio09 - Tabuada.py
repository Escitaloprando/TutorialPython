#faça um progama que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n=int(input('Qual tabuada você quer saber?'))
for o in range(1, 11):
    r=n*o
    #print(n, "x", o, "é igual à", r)
    print('{} X {} é igual à {}'.format(n, o, r))
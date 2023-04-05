#faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
numero=int(input('Qual tabuada você quer saber?'))
for operador in range(1, 11):
    resultado=numero*operador
    #print(n, "x", o, "é igual à", r)
    print('{} X {} é igual à {}'.format(numero, operador, resultado))
#Teste
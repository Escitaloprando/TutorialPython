n1 = float(input('Qual foi sua primeira nota? '))
n2 = float(input('Qual foi sua segunda nota? '))
media = (n1+n2)/2
print('Sua média foi {}'.format(media))
if media < 6.0:
    print('Você reprovou! Estude mais na próxima')
else:
    if media >= 8.0:
        print('Você passou! Parabéns, matou muito bem')
    else:
        print('Você passou! Fez o minimo, dá pra melhorar')
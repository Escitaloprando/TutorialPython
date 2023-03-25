#Faça um programa que leia a largura e a altura de uma parede em metros, cacula a sua área e a quantidade de tinta necessária par apintá-la. sabendo que cada litro de tinta, pinta uma área de 2m²
l=int(input('Qual é a largura da parede?'))
a=int(input('E qual é a altura dela?'))
ar=l*a
print('Essa parede de {}x{}m tem área de {}m² e pra pintar ela vai ser necessário o uso de {} latas de tinta.'.format(l, a, ar, ar/2))
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triángulo 
#retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
#Soh Cah Toa
ca=float(input("insira o cateto adjascente"))
co=float(input('Insira o cateto oposto'))
print('A hipotetuna do triangulo retângulo é {}'.format(math.hypot(ca, co)))

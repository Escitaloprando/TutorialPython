#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
pesos = [int(input('Qual é seu peso em quilos? ')) for _ in range(1, 6)]
print(f'O maior peso foi {max(pesos)}Kg e o menor foi {min(pesos)}Kg.')
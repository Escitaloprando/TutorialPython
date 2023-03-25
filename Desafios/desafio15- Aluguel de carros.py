#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro 
#custa R$60 por dia e R$0.15 por Km rodado
d=int(input('Usou por quantos dias?'))
k=int(input('E rodou quantos quilômetros?'))
p=d*60+k*0.15
print('Tu vai ter o custo de R${:.2f}'.format(p))
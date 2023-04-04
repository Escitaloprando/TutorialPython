# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250.00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Ta ganhando quanto, camarada?'))
if salario <= 1250.0:
    print('Com aumento de 15%, tu vai receber {}'.format(float(salario*1.15)))
else:
    print('Com aumento de 10%, tu vai receber {:.2f}'.format(float(salario*1.10)))
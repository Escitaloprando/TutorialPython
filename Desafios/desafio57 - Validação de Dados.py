# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, 
# faça uma digitação novamente até ter um valor correto.
sexo = "a"
while sexo not in ["M", "F"]:
    sexo = str(input('Qual é seu sexo? [F/M] ')).upper()
print(f'Seu sexo é {sexo}')
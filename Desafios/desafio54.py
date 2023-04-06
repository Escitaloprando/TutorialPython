# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas 
# ainda não atingiram a maioridade e quantas já são maiores de idade.

anos = list() #lista aberta que irá armazenar os anos de nascimento
maiores = 0 #objeto que irá armazenar a contagem de maiores de idade
menores = 0 #objeto que irá armazenar a contagem de menores de idade
for anoNascimento in range(1, 8): # loop que realiza o recebimento e armeza os anos na lista 
    anos.append(int(input('Digite o ano de nascimento ')))
idade = [ 2023-i for i in anos] # realiza acontagem da idade. Subtrai 2023 pelo ano de nascimento inserido
for i in idade: # faz a verificação de maioridade ou minoridade, armazenando em seus respectivos contadores
    if i >= 21:
        maiores += 1
    else:
        menores += 1
print('Existem {} pessoas maiores de idade e {} menores de idade.'.format(maiores, menores)) #print resultado final


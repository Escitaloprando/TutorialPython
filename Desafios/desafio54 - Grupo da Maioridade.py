# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas 
# ainda não atingiram a maioridade e quantas já são maiores de idade.

anos = list() #lista aberta que irá armazenar os anos de nascimento
maiores = 0 #objeto que irá armazenar a contagem de maiores de idade
menores = 0 #objeto que irá armazenar a contagem de menores de idade
for i in range(1, 8): # loop que realiza o recebimento e armeza os anos na lista 
    anos.append(int(input(f'Digite o ano de nascimento da {i}° pessoa: ')))
idade = [ 2023-i for i in anos] # realiza a contagem da idade. Subtrai 2023 pelo ano de nascimento inserido
for i in idade: # faz a verificação de maioridade ou minoridade, armazenando em seus respectivos contadores
    if i >= 21:
        maiores += 1
    else:
        menores += 1
print(f'Existem {maiores} pessoas maiores de idade e {menores} menores de idade.') #print resultado final

# Resolução Guanabara:
# form datetime import date
# atual = date.today().year
# totamaior = 0
# totmenor = 0
# from pess in range(1, 8):
#     nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
#     idade = atual - nasc
#     if idade >= 21:
#         totmaior += 1
#     else:
#         totmenor += 1
# print('Ao todo tivemos {} pessoas maiores de idade.'.format(totmaior))
# print('E também tivemos {} pessoas menores de idade.'.format(totmenor))


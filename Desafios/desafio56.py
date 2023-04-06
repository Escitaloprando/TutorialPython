# Desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre:
# -A média de idade do grupo
# -Qual é o nome do homem mais velho
# -Quantas mulheres tem menos de 20 anos
nome = []
idade = []
sexo = []
maisVelho = []
for _ in range (1, 5):
    nome.append(input('Qual é seu nome? '))
    idade.append(int(input('Qual é sua idade? ')))
    sexo.append(str(input('Você se identifica como Homem(H) ou Mulher(M)? ')))
somaIdades = sum(idade)
mediaIdade = somaIdades / 4
homens = []
mulheres = []
for i in sexo:
    if i == 'H':
        homens = sexo.index(i)
    elif i == 'M':
        mulheres.append(sexo.index(i)) 
print(homens)
print(mulheres)

# Resolução Guanabara
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm': #atribui o primeiro homem às variáveis
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem: #verifica se a idade do homem é maior do que a idade do primeiro, quando verdadeiro, atualiza o valor. No final sendo o maios velho
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade \ 4
print('A média de idade do grupo é de {} anos.'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))

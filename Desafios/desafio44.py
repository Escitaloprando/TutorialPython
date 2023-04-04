# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição
# de pagamento:

# -à vista dinheiro/cheque: 10% de desconto
# -à vista no cartão: 5%
# -em até duas vezes no cartão: preço normal
# -3x ou mais no cartão: 20%
preco = int(input('Insira o valor do produto. '))
pagamento = (input('Como você fará o pagamento? \n [1] À VISTA \n [2] À PRAZO \n Pagamento: '))
if pagamento == "1":
    valorFinal = preco * 0.9
    valorFinalCartao = preco * 0.95
    modalide = (input('E qual vai ser a modalide? \n [1] DINHEIRO \n [2] CHEQUE \n [3] CARTÃO \n Modalidade: '))
    if modalide == "1" or modalide == "2":
        print('Beleza! O preço final será R${}.'.format(valorFinal))
    else:
        print('Beleza! O preço final será R${}.'.format(valorFinalCartao))
else:
    modalide = (input('À prazo fazemos apenas no cartão. Vai fazer em quantos meses? \n [1] 2x \n [2] 3x \n Meses: '))
    if modalide == "1":
        parcela = preco / 2
        print('Beleza! O preço total será R${}, parcelado em 2x deR${}'.format(preco, parcela))
    else:
        valorFinal = preco * 1.2
        parcela = valorFinal / 3
        print('Beleza! O preço total será R${}, parcelado em 3x de R${}'.format(valorFinal, parcela))
   
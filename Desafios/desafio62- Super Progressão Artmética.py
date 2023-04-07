# Melhore o desafio61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
# encerra quando ele disse que quer mostrar 0 termos.
#termo = primeiroTermo+(n-1)*razao
primeiroTermo = int(input('Qual será o primeiro termo da sua Progressão Aritmética? '))
razao = int(input('E qual será a sua razão? '))
n = 0
comando = -1
while comando != 0:
    n += 1
    termo = primeiroTermo+(n-1)*razao
    print(f'O {n}° termo de sua PA é: {termo}')
    comando = int(input('Você quer ver mais um termo? \n[0] NÃO \n[1] SIM \nCOMANDO: '))
    if comando not in [0, 1]:
        print('COMANDO INVÁLIDO')
        comando = int(input('Você quer ver mais um termo? \n[0] NÃO \n[1] SIM \nCOMANDO: '))
print('FIM')
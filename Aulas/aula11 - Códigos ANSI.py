# # ANSI escape sequence
# #    style;text;back
# \033[               m
# # Exemplo
# #\033[0;33;44m

# #Códigos para estilo(existem outros, mas estes funcionam lehor para python)
# 0 - None
# 1 - bold
# 4 - underline
# 7 - negative

# #Códigos para texto
# 30 - branco
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - magenta
# 36 - ciano
# 37 - cinza <-- cor padrão

# #códigos de background
# 40 - branco
# 41 - vermelho
# 42 - verde
# 43 - amarelo
# 44 - azul
# 45 - magenta
# 46 - ciano
# 47 - cinza

#Prática

print('\033[31;30mOi, mãe!\033[m')

nome = "Luiz"
print('Olá, {}{}{}'.format('\033[1;36m', nome, '\033[m'))
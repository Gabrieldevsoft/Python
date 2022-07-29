# Ex.: Ana Maria de Souza
# Primeiro = Ana
# Último: Souza
n = str(input('digite seu nome completo:')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('seu primeiro nome é \033[31m{}\033[m'.format(nome[0]))
print('seu último nome é \033[31m{}\033[m'.format(nome[len(nome)-1]))

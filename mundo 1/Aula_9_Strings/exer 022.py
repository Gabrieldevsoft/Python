
nome = str(input("Digite seu nome:")).strip()

# O nome com todas as letras maiúsculas
print("Nome em maiúsculas: \033[31m{}\033[m.".format(nome.upper()))

# O nome com todas minúsculas
print("Nome em minúsculas: \033[31m{}\033[m.".format(nome.lower()))

# Quantas letras ao todo (sem considerar espaços)
print("Letras ao todo: \033[31m{}\033[m.".format(len(nome) - nome.count(" ")))  # Isso beira a gambiarra

# Quantas letras tem o primeiro nome:
nome = nome.split()
print('O primeiro nome é "\033[31m{}\033[m" e ele tem \033[31m{}\033[m letras.'.format(nome[0], len(nome[0])))

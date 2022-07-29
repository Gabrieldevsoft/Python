frase = str(input("Digite uma frase:")).lower().strip()
# Quantas vezes aparece a letra "a":
print("A letra A aparece \033[31m{}\033[m vezes na frase.".format(frase.count("a")))

# Em que posição ela aparece a primeira vez:
print("A primeira letra A aparece na posição \033[31m{}\033[m.".format(frase.find("a")))

# Em que posição ela aparece a última vez:
print("A última letra A apareceu na posição \033[31m{}\033[m.".format(frase.rfind("a")))

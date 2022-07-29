largura = float(input("Digite a largura:"))
altura = float(input("Digite a altura:"))
area = largura * altura

print("Sua parede tem a dimensão \033[31m{}\033[mx\033[31m{}\033[m e sua área é de \033[31m{}\033[mm².".format(largura, altura, area))

# Cada litro (L) de tinta pinta uma área de 2m².
tinta_necessaria = area / 2
print("Para pintar essa parede, você precisará de \033[31m{}\033[mL de tinta.".format(tinta_necessaria))
# Conferir a resposta porque não sei se entendi o problema. O velho Guilherme continua o mesmo, só que agora com ímpeto suficiente para continuar

n = float(input("Digite o preço de um produto:"))
desconto = n * 5 / 100
print("Na liquidação da loja,esse produto de"
      " \033[31m{:.2f}R$\033[m está com desconto de \033[32m5%\033[m e vai custar apenas \033[31m{:.2f}R$\033[m.".format(n, n - desconto))

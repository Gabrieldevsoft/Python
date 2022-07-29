# Considere R$ 3.27 = US$ 1
n = float(input("Quanto dinheiro você tem:"))
dolar = 3.27
conversao = n / dolar
print("Com \033[31m{}\033[m\033[32mR$\033[m você pode comprar \033[31m{:.2f}\033[m\033[32mUS$\033[m.".format(n, conversao))

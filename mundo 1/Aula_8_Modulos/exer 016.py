# Desafio 16: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import trunc

num = float(input("Digite um número real: "))
# print(math.trunc(num))

print("O valor digitado é \033[31m{}\033[m e a sua porção inteira é \033[31m{}\033[m.".format(num, int(num)))

print("O valor digitado é \033[31m{}\033[m e a sua porção inteira é \033[31m{}\033[m.".format(num, trunc(num)))

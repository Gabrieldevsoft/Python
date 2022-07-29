# Desafio 17: Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input("Cateto oposto:"))
ca = float(input("Cateto adjacente:"))
hipotenusa = hypot(co, ca)

# print("A hipotenusa dos números %.1f e %.1f é: %.1f!" % (co, ca, hipotenusa))
print("A hipotenusa dos números \033[31m{}\033[m e \033[31m{}\033[m é \033[31m{:.2f}\033[m.".format(co, ca, hipotenusa))

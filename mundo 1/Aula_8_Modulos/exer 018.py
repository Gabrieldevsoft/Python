# Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

ang = float(input("Digite um ângulo de uma circunferência:"))

seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print("O ângulo de \033[34m{}\033[m tem o seno de \033[31m{:.2f}\033[m.".format(ang, seno))
print("O ângulo de \033[34m{}\033[m tem o cosseno de \033[31m{:.2f}\033[m.".format(ang, coss))
print("O ângulo de \033[34m{}\033[m tem a tangente de \033[31m{:.2f}\033[m.".format(ang, tang))

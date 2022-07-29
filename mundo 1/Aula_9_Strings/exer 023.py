
# ex.: digite um número: 1834
# unidade: 4
# dezenas: 3
# centenas: 8
# milhares: 1

num = int(input("Digite um número a ser fatiado:"))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Unidade: \033[31m{}\033[m".format(u))
print("Dezena: \033[31m{}\033[m".format(d))
print("Centena: \033[31m{}\033[m".format(c))
print("Milhar: \033[31m{}\033[m".format(m))

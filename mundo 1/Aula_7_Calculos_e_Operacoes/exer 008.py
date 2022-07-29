n = int(input('digite um valor em metros:'))
# print("{} metro(s), convertido(s) em centímetros, é {}cm; convertido(s) em milímetros é {}mm.".format(n, (n*100), (n*1000)))

print("\033[31m{}\033[m metros são \033[31m{}\033[m kilômetros.".format(n, n * 1000))
print("\033[31m{}\033[m metros são \033[31m{}\033[m hectômetros.".format(n, n * 100))
print("\033[31m{}\033[m metros são \033[31m{}\033[m decâmetros.".format(n, n * 10))

print("\033[31m{}\033[m metros são \033[31m{}\033[m metros.".format(n, n * 1))

print("\033[31m{}\033[m metros são \033[31m{}\033[m decímetros.".format(n, n / 10))
print("\033[31m{}\033[m metros são \033[31m{}\033[m centímetros.".format(n, n / 100))
print("\033[31m{}\033[m metros são \033[31m{}\033[m milímetros.".format(n, n / 1000))



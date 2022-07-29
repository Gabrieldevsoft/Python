celsius = float(input("Digite a temperatura em Celsius: "))
farenheit = ((1.8 * celsius) + 32)
print("\033[34m{}ºC\033[m correspondem a \033[31m{:.1f}ºF\033[m.".format(celsius, farenheit))

salario = float(input("Digite seu salário:"))
aumento = salario * 15/100
print("O salário do funcionário, que é de "
      "\033[32m{:.2f}R$\033[m, vai subir para "
      "\033[32m{:.2f}R$\033[m com o aumento de \033[32m15%\033[m.".format(salario, salario + aumento))

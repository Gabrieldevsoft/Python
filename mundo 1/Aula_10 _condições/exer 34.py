salario = float(input('qual é o seu salario:R$'))
if salario <= 1250:
     novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('o salario de \033[31m{:.2f}R$ \033[m passara a ser \033[32m{:.2f}R$\033[m agora'.format(salario,novo))
print('vc ganhou na loteria')
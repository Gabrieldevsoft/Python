
#Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

dias = int(input("Por quantos dias o carro foi alugado: "))  # 8 dias
km = float(input("Quantos km o carro rodou: "))  # 720km

custo_dias = (dias * 60)
custo_km = (km * 0.15)

print("Você andou \033[31m{}km\033[m por \033[31m{}\033[m dias, então o preço a pagar é \033[32m{:.2f}R$\033[m.".format(km, dias, (custo_km + custo_dias)))

# tem que dar R$ 588.00

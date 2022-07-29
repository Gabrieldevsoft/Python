distancia = float(input('qual é a distancia da sua viagem:'))
print('você irá percorrer uma distancia de {:.2f}'.format(distancia))
if distancia <=200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45 # variavel calculou o preço
print('o valor a ser pagor sera {:.2f}'.format(preço))
velocidade= float(input('qual é a velocidade carro: '))
if velocidade > 80:
    print('MULTADO! o seu carro ultrapassou o limite de velocidade de 80km')
    multa = (velocidade-80) * 7
    print('você será multado no valor de {:.2f}'.format(multa))
else:
    print('PARABÉNS!você esta dentro do limite de velocidade')

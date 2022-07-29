print('\033[35m-=\033[m' * 20)
print('analisando o triangulo')
print('\033[36m-=\033[m' * 20)
r1= float(input('primeiro seguimento:'))
r2 = float(input('segundo seguimento:'))
r3 = float(input('terceiro seguimento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os seguimento \033[32mPODEM FORMAR\033[m triângulo')
else:
    print('os seguimento \033[31mNÃO PODEM FORMAR\033[m triângulo')
a = int(input('qual é o primeiro número:'))
b = int(input('qual é o segundo numero:'))
c = int(input('qual é o terceiro número:'))
# verificando o menor numero
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando o maior numero
maior = a
if  b > a  and b > c:
    maior = b
if c > a and c > b:
    maior = c
# verificando o maior

#primeiro método
#print('o valor menor é \033[35m{} \033[m'.format(menor)) #{} cor do inicio e depois do colchetes cor do fim
#print('o valor maior é \033[36m{}\033[m'.format(maior)) #{} cor do inicio e depois do colchetes cor do fim
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
          'amarelo':'\033[33m'}
print('o valor menor {}{}{}'.format(cores['azul'],menor,cores['limpa']))
print(' o valor menor é {}{}{}'.format(cores['amarelo'],menor,cores ['limpa']))
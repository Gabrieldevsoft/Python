from random import randint
from time import sleep # faz o computador aguardar por algum segundos
computador = randint(0, 10) # faz o computador sortear
print('-=-' * 20)
print(' vou pensar em um número entre 0 e 10. tente novamente...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta advinhar
print('processando...')
sleep(3)
if jogador == computador:
   print('PARABENS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))

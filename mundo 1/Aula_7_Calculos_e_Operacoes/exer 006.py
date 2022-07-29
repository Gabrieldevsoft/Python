n = int(input('digite um número:'))
cores = {'limpa':'\033[m','vermelho':'\033[31m','azul':'\033[31m'}
print(' o dobro de {}{}{} é {}{}{}'.format(cores['vermelho'], n,cores['limpa'],cores['vermelho'], n*2,cores['limpa']))
print('o triplo de \33[31m{}\33[m é \33[31m{}\33[m'.format(n, n*3))
print('a raiz quadrada de {}{}{} é {}{:.2f}{}'.format(cores['vermelho'],n,cores['limpa'],cores['vermelho'],n**(1/2),cores['limpa']))
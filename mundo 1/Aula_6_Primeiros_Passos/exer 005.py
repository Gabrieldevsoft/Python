
cores = {'limpa':'\033[m','vermelho':'\033[31m'}
entrada = input('digite algo:')
print('é tipo primitivo?\033[31m{}\033[m'.format(type(entrada)))
print('é numerico?{}{}.{}'.format(cores['vermelho'],entrada.isnumeric(),cores['limpa']))
print('é alphanumérico?{}{}.{}'.format(cores['vermelho'],entrada.isalpha(),cores['limpa']))
print('é um decimal? {}{}.{}'.format(cores['vermelho'],entrada.isdecimal(),cores['limpa']))
print('tem caixa baixa? {}{}.{}'.format(cores['vermelho'],entrada.islower(),cores['limpa']))
print('é espaço em branco?{}{}.{}'.format(cores['vermelho'],entrada.isspace(),cores['limpa']))
print('está em caixa alta? {}{}.{}'.format(cores['vermelho'],entrada.isupper(),cores['limpa']))


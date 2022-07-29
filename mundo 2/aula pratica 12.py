nome = str(input('qual é o seu nome?'))
if nome == 'gabriel':
    print('que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('seu nome é bem popular no brasil')
elif nome in 'Ana Claudia  Jessica  Juliana':
    print('que belo nome feminino')
else:
    print('seu nome é bem normal.')
print('tenha um bom dia , {}!'.format(nome))

nota1 = float(input('primeira nota:'))
nota2 = float(input('segunada nota:'))
print('a média do aluno \033[31m{:.1f}\033[m e do aluno \033[31m{:.1f}\033[m é \033[32m{:.1f}\033[m'.format(nota1,nota2,(nota1 + nota2)/2))
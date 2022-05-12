from datetime import date
ano = int(input('digite o ano que deseja analizar.'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é  {}bissexto{}'.format(ano,'\033[4;33;47m', '\033[m'))
else:
    print('o ano {} não é \033[4m bissexto \033[m'.format(ano))

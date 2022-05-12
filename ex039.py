from datetime import date
ano = int(input('Qual o ano de seu nascimento?'))
if ano == (date.today().year)-18 :
    print('Você deve se alisar esse ano.')
elif ano < (date.today().year) - 18 :
    print('Seu tempo de alistamento já passou.')
else :
    tf = (ano+18) - (date.today().year)
    print('Faltam {} anos para seu alistamento obrigatório.'.format(tf))
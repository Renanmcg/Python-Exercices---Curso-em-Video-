from datetime import date
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = (date.today().year) - ano
if idade > 25:
    print('Atleta master.')
elif 25 >= idade > 19:
    print('Atleta senior.')
elif 19 >= idade > 14:
    print('Atleta junior.')
elif 14 >= idade > 9:
    print('Atleta infantil.')
elif 9 >= idade:
    print('Atleta mirim.')

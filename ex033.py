a = int(input('num 1'))
b = int(input('num 2'))
c = int(input('num 3'))
cores = {'azul':'\033[44m',
        'verm':'\033[41m',
        'limpa': '\033[m'}
menor = a
if b < a and c < a:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor numero é {}{}{}'.format(cores['azul'], menor, cores['limpa']))
print('o maior número é {}{}{}'. format(cores['verm'], maior, cores['limpa']))

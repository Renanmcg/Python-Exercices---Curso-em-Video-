frase = input('igite uma frase').upper().strip()
print('a letra A aparece {} vezes na frase'.format(frase.count('A')))
print(' a primeira esta na posição {}'.format(frase.find('A')+1))
print('a ultima esta na pos {}'.format(frase.rfind('A')+1))

frase = input(('Digite uma frase:')).strip().upper()
palavras = frase.split()#separa as palavras da frase de acordo com os espaços
junto = ''.join(palavras)#junta as palavras desconsiderando os espaços
print('você digitou a frase {}'.format(junto))
inverso = junto[::-1]
'''isso no python. Outro jeito seria :
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print('é um palíndromo')
else:
    print('não é um palíndromo')

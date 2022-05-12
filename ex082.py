num = []
pares = []
ímpares = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N]')
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:  # ou então: elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}.')
print(f'A lista dos pares é {pares}.')
print(f'A lista dos impares é {ímpares}.')
'''ter = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
for c in range(ter, 11, razão):
    print('{}'.format(c), end=' ')
print('finis')'''
ter = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
dec = ter + (10 - 1) * razão
for c in range(ter, dec + razão, razão):
    print('{}'.format(c), end=' ')
print('finis')
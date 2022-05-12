números = [int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: '))]

print(números)
print(f'O maior números é {max(números)}.', end = ', ')
print(f'ele apareceu na {números.index(max(números))+1}ª posição.')
print(f'O menor número é {min(números)}', end = ', ')
print(f'ele aparece na {números.index(min(números))+1}ª posição.')
''''Sic fecit guanabara
listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}.')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Você digitou os valores {listanum}.')
print(f'O maior valor digitado foi {mai} nas posições ', end = '')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end = '')
print()
print(f'O menor valor digitado foi {men} nas posições ', end = '')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end = '')
print()'''
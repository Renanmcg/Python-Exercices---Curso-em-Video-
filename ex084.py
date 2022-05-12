pessoas = list()
dados = []
total = 0
mai = men = 0
while True:
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite o peso da pessoa: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    total += 1  # o Guanabara resolveu sem contador: ele usou len(pessoas) diretamente no print final
    c = str(input('deseja continuar?[S/N]'))
    if c in 'Nn':
        break
print('-+' * 30)
print(f'Ao todo, você cadastrou {total} pessoas.')
print(f'O maior peso foi de {mai}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]} ', end='')
print(f'O menor peso foi de {men}kg. Peso de ', end = '')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}', end='')
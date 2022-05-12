time = []
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))  # inserção de chave com dados a um dicionario preexistente
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}?')))  # inserção de dados em uma lista
    jogador['gols'] = partidas[:]  # cópia da lista
    jogador['total'] = sum(partidas)  # somatória dos gols
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)  # Daqui até o próximo -=-=-= é o cabeçalho
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()  # serve para quebrar linha
print('-=' * 30)
for k, v in enumerate(time):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador?[se 999 para]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print(f' -- Levantamento do Jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'  No jogo {i + 1} fez {g} gols.')
    print('-=' * 40)

print('Volte sempre!')

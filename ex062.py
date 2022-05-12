print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais#total += mais
    while cont <= total:
        print('{} '.format(termo), end='')
        termo += razão
        cont += 1
    print('Pausa.')
    mais = int(input('Quantos números deseja que acrescentemos a esta PA ?'))
print('Progressão finalizadado exibindo {} termos.'.format(total))
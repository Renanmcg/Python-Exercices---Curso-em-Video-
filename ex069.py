toth = tot18 = totm20 = 0
while True:
    idade = int(input('Informe a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1  # tot18 = tot18 + 1
    if sexo == 'M':
        toth += 1  # toth = toth + 1
    if sexo == 'F' and idade < 20:
        totm20 += 1  # totm20 = totm20 +1
    resp = ' '
    while resp not in 'SN':  # se eu tiro o N fica fazendo loop no input que segue ao digitar n.
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de passoas com mais de 18 anos {tot18}.')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'Temos {totm20} mulheres com menos de 20 anos.')

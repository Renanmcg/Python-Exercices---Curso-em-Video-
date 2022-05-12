total = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    cont += 1  # cont = cont + preço-----primeiro contador
    total += preço  # total = total + preço
    if preço >= 1000:
        totmil += 1  # totmil = totmil + 1-------segundo contador, só conta se a condição for satisfeita.
    if cont == 1 or preço < menor:  # se for apenas um produto ou este for de preço inferior a 0
        menor = preço  #  este produto se torna o menor preço
        barato = produto  # e o produto mais barato
    resp = ' '
    while resp not in 'SN':  # ou in 'SsNn' o que nos dispensaria de por .upper()
        resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('fim do programa.'))
print(f'O total da compra foi r$ {total:.2f}')
print(f'temos {totmil} produtos custando mais de r$1000.00')
print(f'o produto mais barato foi {barato} que custa r$ {menor:.2f}')

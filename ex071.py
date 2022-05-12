valor = int(input('Qual valor você deseja sacar?'))
# total = valor .... sic fecit Guanabara, sed mihi melius videtur uti variabile valor  loco secundae variabilis total.
ced = 100
totced = 0
while True:
    if valor >= ced:  # que aqui vale 100. Este primeiro if vai descontar as notas de 100.
        valor -= ced  # valor = valor - ced
        totced += 1  # totced = totced + 1
    else:  # a partir daqui as notas de 100 são grandes demais, por isso é necessário mudar para cédulas de menor valor.
        if valor < ced:  # interessante como solução: porque não por nesse if valor < ced?--- solução guana:if totced
            # > 0:
            print(f'total de {totced} cedulas de R$ {ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        totced = 0
        if valor == 0:
            break

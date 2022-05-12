n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
media = (n1+n2) / 2
if media >= 7:
    print('aprovado')
elif  7 > media > 5:
    print('recuperação')
else:
    print('reprovado')
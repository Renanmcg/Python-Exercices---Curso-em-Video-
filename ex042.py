r1=float(input('seg 1'))
r2=float(input('seg 2'))
r3=float(input('seg 3'))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print('Estes segmentos podem formar um triangulo.')
    if r1 == r2 == r3:
        print('Equilátero.')
    elif r1!= r2 != r3 != r1:
        print('Escaleno.')
    else:
        print('Isóceles.')
else:
    print('Estes segmentos não podem formar triangulo.')

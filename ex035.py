r1 = float(input('seg 1'))
r2 = float(input('seg 2'))
r3 = float(input('seg 3'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34;42m Estes segmentos podem formar um triangulo \033[m')
else:
    print('\033[33;41m Estes segmentos não podem formar triangulo \033[m')

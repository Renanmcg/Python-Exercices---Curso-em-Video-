sal = float(input('salario'))
if sal <= 1250:
    novo = sal + (sal * 15/100)
else:
    novo = sal + ( sal * 10 / 100)
print(' o salario com aumento é {}{}{}'.format('\033[34;42m', novo, '\033[m'))


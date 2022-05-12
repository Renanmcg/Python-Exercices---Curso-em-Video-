'''from math import factorial
n = int(input('digite num para fac: '))
f = factorial(n)
print(' o fatorial de {} é {}.'.format(n, f))'''
n = int(input('Digite um numero para ser fatorado: '))
c = n
f = 1
print('Calculando {}! ='.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f += c
    c -= 1
print('{}'.format(f))

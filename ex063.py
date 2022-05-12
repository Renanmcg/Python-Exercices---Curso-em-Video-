n = int(input('Quantos termos da sequência de Fibonacci você quer mostrar?'))
t1 = 0
t2 = 1
print('{}-{}'.format(t1, t2), end='')
cont = 3 #começa no 3 porque a dita sequência começa invariavelmente em 0, 1, ou seja aqui neste programa a conta começa do terceiro numero: t3
while cont <= n:
    t3 = t1 + t2
    print('-{}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('-Fim!')
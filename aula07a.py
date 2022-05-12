n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1+ n2
sub = n1-n2
d = n1/n2
m = n1*n2
di= n1//n2
p = n1**n2
mod = n1%n2
print('A soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.3f},'.format(s, sub, m, d), end='>>>')
print(' a divisão inteira é {}, a potência é {}, e o resto é {}'.format(di, p, mod))

import math
ca = float(input('valor do cateto adjacente: '))
co = float(input('valor do cateto oposto: '))
hipo = math.sqrt(ca ** 2 + co ** 2)
print('a hipotenusa é {:.3f}'.format(hipo))



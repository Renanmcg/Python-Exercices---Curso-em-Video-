nc = input('Digite seu nome completo: ').strip()
print('seu nome em maiusculas é {}'.format(nc.upper()))
print('seu nome em minusculas é {}'.format(nc.lower()))
print('ele tem {} caracteres,'.format(len(nc)-nc.count(' ')))
#print('seu primeiro nome é {}'.format(nc.find(' ')))
separa = nc.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))







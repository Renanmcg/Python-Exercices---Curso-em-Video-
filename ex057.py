sexo = input('Qual seu sexo?[M/F]').strip().upper()[0]
while not sexo in 'MmFf':
        sexo = input('Sexo invalido. Por favor, digite corretamente.').strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
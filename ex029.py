vel = int(input('qual a sua velocidade?'))
if vel > 80:
    print('\033[30;41m você está multado! Deve pagar {}.\033[m'.format((vel - 80) * 7))
else:
    print('dirija em segurança.')

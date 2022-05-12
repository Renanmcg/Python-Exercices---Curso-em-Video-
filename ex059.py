resultado = 0
opção = ''
while not opção == 0:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))
    print('Qual operação você deseja que seja feita entre estes números?\n [1] soma\n [2]subtração\n [3]multiplicação\n [4]divisão?')
    print('Digite [0] para parar o programa.')
    opção = (input('Insira o número correspondente: '))
    if opção == 1:
        resultado = n1 + n2
        print('O resultado é {}.'.format(resultado))
    elif opção == 2:
        resultado = n1 - n2
        print('O resultado é {}.'.format(resultado))
    elif opção == 3:
        resultado = n1 * n2
        print('O resultado é {:.2f}.'.format(resultado))
    elif opção == 4:
        resultado = n1 / n2
        print('O resultado é {:.2f}.'.format(resultado))
    elif opção not in (0, 1, 2, 3, 4):
        print('Valor invalido.')
print('Fim.')
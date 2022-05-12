def fatorial(n, show=False):
    """
    Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n>
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f += c
    return f


while True:
    n = int(input('Qual valor deseja fatorar?'))
    escolha = str(input('Deseja ver a operação?[S/N]'))
    if escolha in 'Nn':
        print(fatorial(n, show=False))  # esse 'show' serve para ver (True) ou não ver (False) a operação
    else:
        print(fatorial(n, show=True))
    resp = str(input('Quer continuar?'))
    if resp in 'nN':
        break

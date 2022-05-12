from random import randint
v = 1 #contador
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)  # Escolha do pc
    total = jogador + computador  # É o resultado
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I]')).strip().upper()[0]  # Escolha do jogador
    print(f'Você jogou {jogador} e o computador {computador}. total de {v} tentativas.', end='')
    print('Deu par.' if total % 2 == 0 else 'Deu impar.')
    if tipo == 'P':
        if total % 2 == 0:  # par
            print('Você venceu!')
            v += 1  # v = v + 1
        else:  # impar
            print('Você perdeu!')
            break  # se eu perco para e se eu ganho continua e conta tentativas... não seria melhor o contrario? se perde pergunta se quer continuar e conta as tentativas.
    elif tipo == "I":
        if total % 2 == 1:  # impar
            print('Você venceu!')
            v += 1  #v = v +1
        else:  # par
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
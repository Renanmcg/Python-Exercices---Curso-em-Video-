import random #o professor deu uma solução diferente.
from time import sleep
computador = random.randint(0, 2)
pedra = 0
papel = 1
tesoura = 2
print(computador)
jogador = int(input(' Pedra [0], papel [l], tesoura [2]'))
if computador == jogador:
    print('Empate!')
elif computador == papel and jogador == pedra:
    print('O computador ganhou!')
elif computador == papel and jogador == tesoura:
    print('O jogador ganhou!')
elif computador == pedra and jogador == papel:
    print('O jogador ganhou!')
elif computador == pedra and jogador == tesoura:
    print('O computador ganhou!')
elif computador == tesoura and jogador == pedra:
    print(' O jogador ganhou!')
elif computador == tesoura and jogador == papel:
    print('O computador ganhou!')
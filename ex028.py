import random
from time import sleep
cn = random.randint(0, 5)#sorteio de numero
n = int(input('em que número eu pensei?'))#tentativa do jogador
print('processando...')
sleep(2)
if n == cn:
    print('\033[1m Parabens! \033[m Você acertou!')
else:
    print('\033[30;41m Você errou!\033[m eu pensei no número {}'.format(cn))

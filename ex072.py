extenso = 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
while True:
    num = int(input('Digite um número de um a dez para ser escrito por extenso: '))
    if 0 <= num <= 10:
        break
print(f'O número {num} por extenso é {extenso[num - 1]}')

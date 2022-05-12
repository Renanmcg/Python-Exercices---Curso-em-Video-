cont = soma = 0
num = int(input('Digite um número [999 para parar].'))
while num != 999:
    soma += num  # Para a somatoria
    cont += 1  # PARA A CONTA do num de vezes
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))

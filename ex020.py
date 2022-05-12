import random
a1 = input('aluno 1')
a2 = input('aluno 2')
a3 = input('aluno 3')
lista = [a1, a2, a3]
random.shuffle(lista)
print(' Eis a ordem de nomes embaralhada:')
print(lista)

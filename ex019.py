#Um professor quer sortear um dos seus quatro alunos para apagar o quadro> Faça um programa que ajuda ele lendo o nome deles e escrevendo o nome do escolhido
import random
al1 = input('aluno um: ')
al2 = input('aluno dois: ')
al3 = input('aluno três: ')
lista = [al1, al2, al3]
el = random.choice(lista)
print('O quadro deverá ser apagado por {}.'.format(el))

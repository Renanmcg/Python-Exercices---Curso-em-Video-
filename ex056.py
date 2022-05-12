somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    nome = str(input('Qual o nome da {}º pessoa?'.format(c)))
    idade = int(input('Qual a idade da {}º pessoa?'.format(c)))
    sexo = str(input('Qual o sexo da {}º pessoa?[M/F]'.format(c)))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/c
print('A media de idade do grupo é {}.'.format(mediaidade))
print('O nome do homem + velho é {}.'.format(nomevelho))
print('São {} mulherres com menos de vinte anos.'.format(totmulher20))
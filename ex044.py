preço = float(input('Digite o valor: '))
fordpag = input('''Qual forma de pagamento 
[1] a vista em dinheiro
[2] a vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
if fordpag == '1':
    preçof = preço - (preço * 10 / 100)
    print('O valor a pagar será {}, o senhor teve 10% de desconto.'.format(preçof))
elif fordpag == '2':
    preçof = preço - (preço * 5 / 100)
    print('O valor a pagar será {}, o senhor teve 5% de desconto.'.format(preçof))
elif fordpag == '3':
    preçof = preço
    print('O senhor não terá desconto.')
elif fordpag == '4':
    preçof = preço + (preço * 20 / 100)
    print('Assim o valor será de {} com 20% de juros.'.format(preçof))
else :
    print('Opção invalida.')
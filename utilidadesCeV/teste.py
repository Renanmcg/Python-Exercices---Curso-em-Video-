from utilidadesCeV import moeda, Dado

#preço = float(input('Digite o preço: R$'))
#moeda.resumo(preço, 34, 45)

p = Dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
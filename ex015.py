d = 60
km = 0.15
dus = int(input('quantos dias?'))
kmr = float(input('quantos km?'))
pkm = km*kmr
pd = dus * d
print('vo deve pagar {} pelos dias, {} pelos km rodados e o total é {}'.format(pd, pkm, pkm+pd))

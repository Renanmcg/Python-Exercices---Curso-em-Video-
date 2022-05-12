dist = int(input('Digite a distância em kilometros de sua viagem.'))
preço = dist * 0.5
preçop = dist * 0.45
if dist < 200:
    print('o preço será {}'.format(preço))
else:
    print('o preço será {}'.format(preçop))
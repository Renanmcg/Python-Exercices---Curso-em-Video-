peso = float(input('Digite seu peso:'))
alt = float(input('Digite sua altura:'))
imc = peso/alt**2
print('Seu imc é {:.2f}.'.format(imc))
if imc > 40:
    print('Obesidade morbida.')
elif 40 >= imc > 30:
    print('Obesidade.')
elif 30 >= imc >25:
    print('Sobrepeso.')
elif 25 >= imc > 18.5:
    print('Peso ideal.')
elif 18.5 >= imc:
    print('Abaixo do peso.')

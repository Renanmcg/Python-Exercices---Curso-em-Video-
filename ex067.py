while True:
    n = int(input('Quer ver a tabuada de qual valor?'))
    if n < 0 :# quia voluit Guanabara
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
print('NO!!!')
pcasa = float(input('Qual o valor da casa?'))
sal = float(input('Qual é o seu salario?'))
prazo = float(input('Em quantos anos deseja pagar?'))
nmens = prazo * 12
mens = pcasa/nmens
if mens <= (sal * 30 / 100):
    print('O empréstimo lhe será concedido')
else :
    print('O emprestimo não lhe será concedido')

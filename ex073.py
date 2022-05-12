times = 'São Paulo', 'Palmeiras', 'Santos'
print(f'Lista de times {times}.')
print(f'Os primeiros 5 são {times[0:5]}.')
print(f'Os quarto últimos sao {times[-4:]}.')
print(f'Em ordem alfabetica {sorted(times)}.')
print(f'O São Paulo está na {times.index("São Paulo")+1}  posição.')
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional.'
    else:
        return f'Com {idade} anos: Voto obrigatório.'


while True:  # com melhorias usando o tratamento de erros.
    try:
        idade = int(input(' Digite o ano de nascimento: '))
        print(voto(idade))
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'Nn':
            break

    except ValueError:
        print('Valor inválido!')

    except IndexError:
        print('Erro! Informação inválida.')
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]


def notas(*n, sit=False):
    """
    Função para analisar notas e situações de diferentes alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adcionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """

    r = {}  # ou    r = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': sum(n) / len(n)}
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


resp = notas(10, 5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)

def notas(*valores, status=False):
    """
    -> Boletim de várias notas
    :param valores: recebe múltiplos valores
    :param status: se status=True mostra situação da média
    :return: dicionário com Total, Maior, Menor e Média das notas
    """
    y = dict()
    y['Total'] = len(valores)
    y['Maior'] = max(valores)
    y['Menor'] = min(valores)
    y['Media'] = sum(valores) / len(valores)
    if status:
        if y['Media'] >= 7:
            y['Situação'] = 'Favorável'
        elif 4 <= y['Media'] < 7:
            y['Situação'] = 'Razoável'
        else:
            y['Situação'] = 'Péssima'
    return y



resp = notas(6.2, 6.2, 9, status=True)
print(resp)
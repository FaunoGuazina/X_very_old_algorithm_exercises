def METADE(x=0, formato=False):
    metade = x / 2
    return metade if formato is False else MOEDA(metade)


def DOBRO(x=0, formato=False):
    dobro = x * 2
    return dobro if formato is False else MOEDA(dobro)


def AUMENTA(x=0, y=0, formato=False):
    aumenta = x + (x * y / 100)
    return aumenta if formato is False else MOEDA(aumenta)


def DIMINUI(x=0, y=0, formato=False):
    diminui = x - (x * y / 100)
    return diminui if formato is False else MOEDA(diminui)


def MOEDA(x=0, y='€'):
    return f'{y}{x:.2f}'.replace('.', ',')


def RESUMO(x=0, y=0, z=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'{"Preço Analisado:":<20}{MOEDA(x):>10}')
    print(f'{"Dobro do Preço:":<20}{DOBRO(x, True):>10}')
    print(f'{"Medade do Preço:":<20}{METADE(x, True):>10}')
    print(f'{y:>2}{"% de Aumento:":<18}{AUMENTA(x, y, True):>10}')
    print(f'{z:>2}{"% de Redução:":<18}{DIMINUI(x, z, True):>10}')
    print('-' * 30)

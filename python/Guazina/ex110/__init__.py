from Guazina import ex107, ex108


def resumo(x, y=0, z=0):
    valor = ex108.formaEURO(x)
    metade = ex108.formaEURO(ex107.moedaMETADE(x))
    dobro = ex108.formaEURO(ex107.moedaDOBRO(x))
    aumenta = ex108.formaEURO(ex107.moedaAUMENTA(x, y))
    diminui = ex108.formaEURO(ex107.moedaDIMINUI(x, z))
    return print('-' * 30), \
           print(f'{"RESUMO DO VALOR":^30}'), \
           print('-' * 30), \
           print(f'{"Preço Analisado:":<20}{valor:>10}'), \
           print(f'{"Dobro do Preço:":<20}{dobro:>10}'), \
           print(f'{"Medade do Preço:":<20}{metade:>10}'), \
           print(f'{y:>2}{"% de Aumento:":<18}{aumenta:>10}'), \
           print(f'{z:>2}{"% de Redução:":<18}{diminui:>10}'), \
           print('-' * 30)

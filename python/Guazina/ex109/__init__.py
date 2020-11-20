from Guazina import ex108, ex107
def METADE(x, exibir=False):
    metade = ex107.moedaMETADE(x)
    if exibir:
        return ex108.formaEURO(metade)
    else:
        return metade


def DOBRO(x, exibir=False):
    dobro = ex107.moedaDOBRO(x)
    if exibir:
        return ex108.formaEURO(dobro)
    else:
        return dobro


def AUMENTA(x, y, exibir=False):
    aumenta = ex107.moedaAUMENTA(x, y)
    if exibir:
        return ex108.formaEURO(aumenta)
    else:
        return aumenta


def DIMINUI(x, y, exibir=False):
    diminui = ex107.moedaDIMINUI(x, y)
    if exibir:
        return ex108.formaEURO(diminui)
    else:
        return diminui


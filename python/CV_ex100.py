from random import randint


def sorteio(qtd, lista):
    for n in range(qtd):
        n = randint(1, 10)
        lista.append(n)
    print(lista)

def somaPAR(lista):
    par = 0
    for v in lista:
        if v % 2 == 0:
            par += v
    print(f'A doma dos pares é {par}')


num = list()
sorteio(5, num)
somaPAR(num)
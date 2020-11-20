def fatorial(valor, exibir=False):
    """
    -> Cálculo de fatorial de um determinado valor
    :param valor: número a ser calculado
    :param exibir: opcional se mostra o cálculo
    :return: o valor fatorial do valor indicado
    """
    fator = 1
    for c in range(valor, 0, -1):
        fator *= c
        if exibir:
            if c == 1:
                print(c, end=' = ')
                break
            print(c, end=' x ')
    return print(fator)


while True:
    numero = int(input('FATORIAL Nº: '))
    x = str(input('Exibir o cálculo [s/n]: ')).strip().lower()[0]
    if x in 'n':
        x = False
    else:
        x = True
    fatorial(numero, exibir=x)
    print('~' * 25)
    quest = ' '
    while quest not in 'SN':
        quest = str(input('Continuar? ')).strip().upper()[0]
    if quest == 'N':
        break
help(fatorial)
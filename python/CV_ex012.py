print('=ˆ= ' * 11)
print('           CÁLCUL DE DESCOMPTES')
print('=ˆ= ' * 11)
valor = float(input('Introduïu l\'import del producte: '))
print('-.- ' * 11)
descompte = float(input('Introduïu l\'import del descompte: '))
print('!<>!' * 11)
print('el valor del vostre producte rebaixat és € {:.2f}'.format(valor - (valor * descompte / 100)))

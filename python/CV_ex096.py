print('==' * 20)
print(f'{"FUNÇÃO ÁREA":^40}')
print('==' * 20)


def área(l, c):
    a = l * c
    print(f'A área do terreno {l}x{c} é {a}m²')


x = float(input('Largura: '))
y = float(input('Comprimento: '))
área(x, y)

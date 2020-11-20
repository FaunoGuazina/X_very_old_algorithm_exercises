print('=ˆ= ' * 8)
print('    TAULA DE MULTIPLICACIÓ')
print('=ˆ= ' * 8)
num = int(input('introduïu un número per trobar\nla taula de multiplicació: '))
print(' ' * 7, '-' * 13)
x = 1
for c in range(1, 11):
    print(' ' * 7, '{} x {:2} = {:3}'.format(num, x, num*x))
    x += 1
print(' ' * 7, '-' * 13)
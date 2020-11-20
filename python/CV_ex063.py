print('{:=^27}'.format(' FIBONACCI '))
quant = int(input('Quantos termos deseja: '))
cont = 3
x = 0
y = 1
print(x, '>', y, '>', end=' ')
while cont <= quant:
    z = x + y
    print(z, '>', end=' ')
    x = y
    y = z
    cont += 1
print('fim')

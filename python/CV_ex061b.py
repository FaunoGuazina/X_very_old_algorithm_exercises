termo = int(input('termo: '))
razao = int(input('razão: '))
quant = int(input('quantidade: '))
for cont in range(1, quant + 1):
    print(termo, '>', end=' ')
    termo += razao
print('acabou')
print(cont)

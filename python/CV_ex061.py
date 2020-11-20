termo = int(input('termo: '))
razao = int(input('razão: '))
quant = int(input('Quantidade: '))
cont = 0
while cont < quant:
    print(termo, '>', end=' ')
    termo += razao
    cont += 1
print('acabou')
print(cont)

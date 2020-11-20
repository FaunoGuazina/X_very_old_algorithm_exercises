termo = int(input('termo: '))
razao = int(input('razão: '))
decimo = termo + (10-1) * razao
cont = 0
for c in range(termo, decimo+razao, razao):
    print(c, end=(' > '))
    cont += 1
print('acabou')
print(cont)

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('peso da {}ª pessoa'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o menor peso foi {}kg e o meio foir {}kg'.format(menor, maior))
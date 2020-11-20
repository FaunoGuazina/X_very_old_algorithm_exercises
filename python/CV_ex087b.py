print('-+' * 14)
print(f'{"Matriz 3x3 PLUS":^28}')
print('-+' * 14)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = somacol3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'numero da posição ({l}, {c}): '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
print('-+' * 14)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()
    somacol3 += matriz[l][2]
print('-+' * 14)
print(f'A soma dos valores pares é {pares}')
print(f'A soma da 3ª coluna é {somacol3}')
print(f'O maior valor da 2ª linha é {max(matriz[1])}')

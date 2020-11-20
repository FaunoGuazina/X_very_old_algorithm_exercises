print('-+' * 14)
print(f'{"Matriz 3x3":^28}')
print('-+' * 14)
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'numero da posição ({l}, {c}): '))
print('-+' * 14)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()

print('-+' * 16)
print(f'{"Matriz 3x3 PLUS":^32}')
print('-+' * 16)
n = list()
p = par = 0
while p < 3:
    for x in range(0, 3):
        x = int(input(f'numero da posição ({p}, {x}): '))
        n.append(x)
        if x % 2 == 0:
            par += x
    p += 1
print('-+' * 16)
print(f'[ {n[0]} ] [ {n[1]} ] [ {n[2]} ]')
print(f'[ {n[3]} ] [ {n[4]} ] [ {n[5]} ]')
print(f'[ {n[6]} ] [ {n[7]} ] [ {n[8]} ]')
print('-+' * 16)
print(f'A soma dos valores pares é: {par}')
print(f'A soma da 3ª coluna é: {n[2] + n[5] + n[8]}')
if n[3] > n[4] and n[3] > n[5]:
    print(f'O maior Nº da 2ª linha é: {n[3]}')
elif n[4] > n[3] and n[4] > n[5]:
    print(f'O maior Nº da 2ª linha é: {n[4]}')
else:
    print(f'O maior Nº da 2ª linha é: {n[5]}')

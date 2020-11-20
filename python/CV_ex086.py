print('-+' * 14)
print(f'{"Matriz 3x3":^28}')
print('-+' * 14)
n = list()
p = 0
while p < 3:
    for x in range(0, 3):
        x = int(input(f'numero da posição ({p}, {x}): '))
        n.append(x)
    p += 1
print('-+' * 14)
print(f'[ {n[0]} ] [ {n[1]} ] [ {n[2]} ]')
print(f'[ {n[3]} ] [ {n[4]} ] [ {n[5]} ]')
print(f'[ {n[6]} ] [ {n[7]} ] [ {n[8]} ]')

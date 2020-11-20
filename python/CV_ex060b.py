fator = int(input('valor fatorial: '))
f = 1
for c in range(fator, 0):
    print(c, 'x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f)
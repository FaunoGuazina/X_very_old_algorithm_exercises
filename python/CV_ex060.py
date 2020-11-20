fator = int(input('valor fatorial: '))
c = fator
f = 1
while c > 0:
    print(c, 'x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f)
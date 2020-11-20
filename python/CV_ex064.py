c = x = y = 0
while x != 999:
    x = int(input('Digite 999 pra parar: '))
    if x != 999:
        y += x
        c += 1
print('vc digitou {} números e a soma deles é {}'.format(c, y))

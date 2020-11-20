c = y = 0
while True:
    x = int(input('Digite 999 pra parar: '))
    if x == 999:
        break
    y += x
    c += 1
print('vc digitou {} números e a soma deles é {}'.format(c, y))

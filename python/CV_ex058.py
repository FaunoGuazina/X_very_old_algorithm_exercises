print('=ˆ= ' * 8)
print('{:^32}'.format('Adivinha o Número'))
print('=ˆ= ' * 8)
from random import randint
pc = randint(1, 10)
acerto = False
c = 0
while not acerto:
    player = int(input('Tenta seu palpite: '))
    c += 1
    if player == pc:
        acerto = True
    else:
        if player < pc:
            print('tente maior...')
        elif player > pc:
            print('tente menor...')
print('vc tentou {} vezes até acertar!!!'.format(c))

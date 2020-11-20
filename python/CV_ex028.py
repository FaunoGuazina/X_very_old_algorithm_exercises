print('=ˆ= ' * 11)
print('        endevina els números')
print('=ˆ= ' * 11)
from random import randint
from time import sleep
num = int(input('triar un nombre de 0 a 10: '))
NUM = randint(0, 10)
print('processament ...')
sleep(3)
if num == NUM:
    print('ho tens bé!!! el número dibuixat era {}'.format(NUM))
else:
    print('Heu fallat!!! el número dibuixat era {}'.format(NUM))

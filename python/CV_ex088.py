print('-+' * 20)
print(f'{"PALPITE DA MEGA":^40}')
print('-+' * 20)
from random import randint
from time import sleep
jogos = int(input('Quantos jogos? '))
print('Gerando combinações...')
sleep(1)
for x in range(1, jogos+1):
    print(f'{x}º Jogo:',
        randint(1, 60), randint(1, 60), randint(1, 60),
         randint(1, 60), randint(1, 60), randint(1, 60))
    sleep(1)
print('-+' * 20)

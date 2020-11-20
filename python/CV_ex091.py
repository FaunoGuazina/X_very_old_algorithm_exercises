print('==' * 20)
print(f'{"4 DADOS":^40}')
print('==' * 20)
from random import randint
from operator import itemgetter
from time import sleep
jogos = dict()
for d in range(4):
    dados = randint(1, 6)
    print(f"Jogador 0{d + 1} jogou {dados}")
    jogos[f'Jogador 0{d + 1}'] = dados
    sleep(.5)
JOGOS = sorted(jogos.items(), key=itemgetter(1), reverse=True)
sleep(1)
print('==' * 20)
for p, x in enumerate(JOGOS):
    print(f"{p+1}º Posição = {x[0]} com {x[1]}")
    sleep(.5)
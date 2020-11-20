print('-+' * 17)
print(f'{"PALPITE DA MEGA":^34}')
print('-+' * 17)
from random import randint
from time import sleep
jogos = list()
quantidade = int(input('     Quantos jogos deseja? '))
contador = 0
print('-+' * 17)
sleep(1)
while contador < quantidade:
    palpite = list()
    itens = 6
    while itens > len(palpite):
        numero = randint(1, 60)
        if numero not in palpite:
            palpite.append(numero)
    palpite.sort()
    jogos.append(palpite)
    contador += 1
for j in range(0, len(jogos)):
    print(f'{j+1}º JOGO:', jogos[j])
    sleep(1)
print('-+' * 5, ' BOA SORTE! ', '-+' * 5)

from random import randint
from time import sleep
jokempo = ['PEDRA', 'TESOURA', 'PAPEL']
print('{:=^25}'.format('=JO'))
sleep(.5)
print('{:=^25}'.format('KEM'))
sleep(.5)
print('{:=^25}'.format('PO'))
sleep(.5)
print('''Suas opções são:
0 = PEDRA
1 = TESOURA
2 = PAPEL''')
player = int(input('Qual sua jogada? '))
if player == 0 or player == 1 or player == 2:
    pc = randint(0, 2)
    print('{:=^25}'.format('JO'))
    sleep(1)
    print('{:=^25}'.format('KEM'))
    sleep(1)
    print('{:=^25}'.format('=PO'))
    sleep(1)
    print('PC escolheu {}'.format(jokempo[pc]))
    sleep(1)
    print('Você escolheu {}'.format(jokempo[player]))
    sleep(1)
    print('{:=^25}'.format(' RESULTADO '))
    sleep(2)
    if pc == 0: # PEDRA
        if player == 0:
            print('{:*^25}'.format(' EMPATOU '))
        elif player == 1:
            print('{:*^25}'.format(' VOCÊ PERDEU '))
        elif player == 2:
            print('{:*^25}'.format(' VOCÊ GANHOU '))
    elif pc == 1: # TESOURA
        if player == 0:
            print('{:*^25}'.format(' VOCÊ GANHOU '))
        elif player == 1:
            print('{:*^25}'.format(' EMPATOU '))
        elif player == 2:
            print('{:*^25}'.format(' VOCÊ PERDEU '))
    elif pc == 2: # PAPEL
        if player == 0:
            print('{:*^25}'.format(' VOCÊ PERDEU '))
        elif player == 1:
            print('{:*^25}'.format(' VOCÊ GANHOU '))
        elif player == 2:
            print('{:*^25}'.format(' EMPATOU '))
else:
    print('{:*^25}'.format('JOGADA INVALIDA'))

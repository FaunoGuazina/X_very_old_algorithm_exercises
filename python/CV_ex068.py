print('~' * 20)
print('{:~^20}'.format(' Par ou Ímpar '))
print('~' * 20)
from random import randint
jogadas = 0
while True:
    playJ = str(input('Par ou Ímpar: ')).strip().upper()[0]
    while playJ[0] not in 'IPÍ':
        print('OPÇÃO INVALIDA!!!')
        playJ = str(input('Par ou Impar: ')).strip().upper()[0]
    if playJ == 'Í':
        playJ == 'I'
    playN = int(input('Escolha um número: '))
    pcN = randint(0, 10)
    soma = playN + pcN
    jogadas += 1
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print('=' * 20)
    print(f'Você escolheu {playN}\nComputador jogou {pcN}\nA soma é {soma}\nO resultado é {resultado}')
    print('=' * 20)
    if resultado[0] == playJ[0]:
        print('{:^20}'.format('Você Ganhou!!!'))
        print('~' * 20)
    else:
        print('{:^20}'.format('Você Perdeu!!!'))
        print('~' * 20)
        jogadas -= 1
        break
print('{:!^20}'.format(' GAME OVER '))
print('{:^20}'.format(f'Vc venceu {jogadas} partidas'))

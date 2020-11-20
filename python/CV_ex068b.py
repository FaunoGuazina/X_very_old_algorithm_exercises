print('~' * 20)
print('{:~^20}'.format(' Par ou Ímpar '))
print('~' * 20)
from random import randint
jogadas = 0
while True:
    playJ = str(input('Par ou Ímpar? ')).strip().upper()[0]
    while playJ[0] not in 'IPÍ':
        print('OPÇÃO INVALIDA!!!')
        playJ = str(input('Par ou Ímpar? ')).strip().upper()[0]
    if playJ == 'Ii':
        playJ == 'Í'
    playN = int(input('Escolha um número: '))
    pcN = randint(0, 10)
    jogadas += 1
    soma = playN + pcN
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print('=' * 20)
    print('{:^20}'.format(f'VC = {playN} | PC = {pcN}'))
    print('{:^20}'.format('> RESULTADO <'))
    print('{:^20}'.format(f'{soma} <> {resultado}'))
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
if jogadas > 1:
    print('{:^20}'.format(f'Vc venceu {jogadas} partidas'))
elif jogadas == 1:
    print('{:^20}'.format(f'Vc venceu {jogadas} partida'))
else:
    print('{:^20}'.format('NÃO VENCEU NENHUMA'))

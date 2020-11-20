print('==' * 20)
print(f'{"Aproveitamento Gols":^40}')
print('==' * 20)
jogador = dict()
jogador['Nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Nº de partidas de {jogador["Nome"]}? '))
gols = list()
jogador['Total'] = 0
for x in range(partidas):
    x = int(input(f'Qts gols na {x + 1}ª partida: '))
    gols.append(x)
    jogador['Total'] += x
jogador['Gols'] = gols
print('==' * 20)
for k, v in jogador.items():
    print(f'{k}: {v}')
    if k == 'Gols':
        for p, v in enumerate(jogador['Gols']):
            print(f'Na {p+1}ª partida foram {v} Gol(s)')

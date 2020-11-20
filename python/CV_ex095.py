print('==' * 20)
print(f'{"Aproveitamento Gols":^40}')
print('==' * 20)
time = list()
while True:
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
    time.append(jogador)
    quest = ' '
    while quest not in 'SN':
        quest = str(input('CONTINUAR [S/N]? ')).strip().upper()[0]
    if quest == 'N':
        break
print('==' * 20)
print(f"{'Cod'}{'Nome':^15}{'Gols':^15}{'TOTAL'}")
print('-' * 41)
for x in time:
    print(f"{time.index(x) + 1:^3}{x['Nome']:^15}{str(x['Gols']):^15}{x['Total']:^5}")
print('_' * 41)
while True:
    escolha = int(input('DETALHAR JOGADOR? Cod: '))
    for x in time:
        if time.index(x) == (escolha-1):
            print(f'Detalhamento jogador {x["Nome"]}')
            for p, v in enumerate(x['Gols']):
                print(f'Partida {p+1} = {v} gol(s)')
    print('_' * 41)
    quest = ' '
    while quest not in 'SN':
        quest = str(input('CONTINUAR [S/N]? ')).strip().upper()[0]
    if quest == 'N':
        break
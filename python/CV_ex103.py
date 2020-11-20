def ficha(jogador=0, gols=0):
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '':
        gols = 0
    return print(f'O jogador {jogador} fez {gols} no campeonato')


nome = str(input('Nome do Jogador: '))
valor = str(input('Quantos gols: '))
ficha(nome, valor)

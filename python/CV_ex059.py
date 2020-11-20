v1 = float(input('PRIMEIRO VALOR: '))
v2 = float(input('SEGUNDO  VALOR: '))
option = int(input('''Escolha a ação desejada:\n[1] SOMA\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NúMEROS\n[5] SAIR DO PROGRAMA\nEscolha a opção desejada: '''))
while option in range(1, 6):
    if option == 1:
        print('Resultado de {} + {} = {}'.format(v1, v2, v1 + v2))
        option += 5
        print('fim')
    if option == 2:
        print('resultado de {} x {} = {}'.format(v1, v2, v1 * v2))
        option += 4
        print('fim')
    if option == 3:
        if v1 == v2:
            print('Os valores {} e {} são iguais'.format(v1, v2))
        if v1 > v2:
            print('{} é maior que {}'.format(v1, v2))
        if v2 > v1:
            print('{} é maior que {}'.format(v2, v1))
        option += 3
        print('fim')
    if option == 4:
        v1 = float(input('PRIMEIRO VALOR: '))
        v2 = float(input('SEGUNDO  VALOR: '))
        option = int(input('''Escolha a ação desejada:\n[1] SOMA\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NúMEROS\n[5] SAIR DO PROGRAMA\nEscolha a opção desejada: '''))
    if option == 5:
        option += 1
        print('fim')

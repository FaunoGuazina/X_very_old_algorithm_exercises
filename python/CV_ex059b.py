from time import sleep
v1 = float(input('PRIMEIRO VALOR: '))
v2 = float(input('SEGUNDO  VALOR: '))
option = 0
while option != 5:
    print('''Escolha a ação desejada:\n[1] SOMA\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NúMEROS\n[5] SAIR DO PROGRAMA''')
    option = int(input('>.>.> Qual sua escolha? '))
    if option == 1:
        print('A soma entre {} + {} = {}'.format(v1, v2, v1 + v2))
    elif option == 2:
        print('O produto entre {} x {} = {}'.format(v1, v2, v1 * v2))
    elif option == 3:
        if v1 > v2:
            print('Primeiro valor {} é maior que Segundo valor {}'.format(v1, v2))
        elif v2 > v1:
            print('Segundo valor {} é maior que primeiro valor {}'.format(v2, v1))
        elif v1 == v2:
            print('Ambos os valores {} e {} são iguais'.format(v1, v2))
    elif option == 4:
        print('Digite os valores novamente:')
        v1 = float(input('PRIMEIRO VALOR: '))
        v2 = float(input('SEGUNDO  VALOR: '))
    elif option == 5:
        print('finalizando...')
    else:
        print('opção invalída, tente novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa, volte sempre!')

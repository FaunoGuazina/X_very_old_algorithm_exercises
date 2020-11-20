valor = list()
while True:
    valor.append(int(input('Adicione um valor: ')))
    if len(valor) > 1:
        if valor[-1] in valor[0:-1]:
            print('valor duplicado não inserido')
            valor.pop()
    quest = ' '
    while quest[0] not in 'SN':
        quest = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if quest == 'N':
        break
print('=' * 30)
print(f'Você digitou os valores {sorted(valor)}')

'''SOLUÇÃO GUANABARA
        n = int(input('Adicione um valor: '))
            if n not in valor:
                valor.append(n)
                print('valor inserido com sucesso')
            else:
                print('valor duplicado não inserido')
'''
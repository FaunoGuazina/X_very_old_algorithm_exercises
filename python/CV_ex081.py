valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    quest = ' '
    while quest[0] not in 'SN':
        quest = str(input('Deseja continuar?')).strip().upper()
    if quest[0] == 'N':
        break
valoresR = sorted(valores, reverse=True)
print(f'a quantidade de valores digitada foi {len(valores)}')
print(f'em ordem decrescente foram {valoresR}')
if 5 in valoresR:
    print('o valor 5 faz parte da lista na posição(ões):', end=' ')
    for p, v in enumerate(valoresR):
        if v == 5:
            print(p, end=' ')
else:
    print('o valor 5 não faz parte da lista')

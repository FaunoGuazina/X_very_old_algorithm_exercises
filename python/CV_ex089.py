print('==' * 20)
print(f'{"BOLETIM DE NOTAS":^40}')
print('==' * 20)
boletim = list()
while True:
    aluno = list()
    notas = list()
    n = str(input('aluno: ')).strip().title()
    aluno.append(n)
    n1 = float(input('1ª NOTA: '))
    notas.append(n1)
    n2 = float(input('2ª NOTA: '))
    notas.append(n2)
    aluno.append(notas)
    boletim.append(aluno)
    q = ' '
    while q not in 'SN':
        q = str(input('continuar [s/n]?')).strip().upper()[0]
    if q == 'N':
        break
print('_' * 25)
print(f'Nº {"NOME":<15} MÉDIA')
print('_' * 25)
for x in range(0, len(boletim)):
    print(f'{x+1}  {f"{boletim[x][0]}":<15}  {(boletim[x][1][0] + boletim[x][1][1]) / 2:.2f}')
print('_' * 25)
while True:
    q = ' '
    while q not in 'SN':
        q = str(input('CONFERIR NOTAS? [s/n]?')).strip().upper()[0]
    if q == 'N':
        break
    a = int(input('Qual Nº do Aluno? '))
    while a > len(boletim):
        print('Nº de aluno inexistente')
        a = int(input('Qual Nº do Aluno? '))
    print(f'As notas de {boletim[a - 1][0]} foram {boletim[a - 1][1]}')
print('OBRIGADO, VOLTE SEMPRE!!!')

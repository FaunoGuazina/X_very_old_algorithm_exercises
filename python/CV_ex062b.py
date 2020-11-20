primeiro = int(input('termo: '))
razao = int(input('razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, '>', end=' ')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos mais vc deseja? '))

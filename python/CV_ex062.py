print('{:=^20}'.format(' Gerador P.A. '))
termo = int(input('Primeiro termo: '))
razao = int(input('Qual a razão: '))
quant = int(input('Quantos termos: '))
cont = 1
total = 0
mais = quant
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, '>', end=' ')
        termo += razao
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos mais vc deseja? '))
print('progressão finalizada com {} termos demosntrados'.format(total))
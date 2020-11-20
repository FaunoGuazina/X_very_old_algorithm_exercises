n = c = y = maior = menor = 0
q = 'S'
while q == 'S':
    n = int(input('digite um número: '))
    c += 1
    y += n
    if c == 1:
        menor = maior = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    q = str(input('Quer continuar, Sim ou não? ')).strip().upper()[0]
print('vc digitou {} valores e a média entre eles é {}'.format(c, y / c))
print('o menor valor digitado foi {} e o maior foi {}'.format(menor, maior))

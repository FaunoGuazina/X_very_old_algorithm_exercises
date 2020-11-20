print('{:-^30}'.format(' BANCO FAUNO '))
print('~'*30)
saque = int(input('Qual valor deseja sacar? '))
total = saque
ced = 100
xced = 0
print('$'*30)
while True:
    if total >= ced:
        total -= ced
        xced += 1
    else:
        if xced > 0:
            print('{:.^30}'.format(f'{xced} cédulas de {ced:.2f}'))
            xced = 0
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 1
        if total == 0:
            break
print('{:-^30}'.format(' VOLTE SEMPRE '))

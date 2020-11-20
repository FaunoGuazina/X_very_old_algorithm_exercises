saque = int(input('Qual valor deseja sacar? '))
u = saque // 1 % 10
d = saque // 10 % 10
c = saque // 100 % 10
m = saque // 1000 % 10
cd1 = cd2 = cd5 = cd10 = cd20 = cd50 = cd100 = 0
while u != 0:
    if u == 5:
        cd5 += 1
    elif u < 5:
        if (u % 2) == 0:
            cd2 += (u // 2)
        else:
            cd1 += 1
            if u > 1:
                cd2 += 1
    else:
        cd5 += 1
        if (u % 2) == 1:
            cd2 += ((u - 5) // 2)
        else:
            cd1 += 1
            if u > 6:
                cd2 += 1
    break
while d != 0:
    if d == 5:
        cd50 += 1
    elif d < 5:
        if (d % 2) == 0:
            cd20 += (d // 2)
        else:
            cd10 += 1
            if d > 1:
                cd20 += 1
    else:
        cd50 += 1
        if (d % 2) == 1:
            cd20 += ((d - 5) // 2)
        else:
            cd10 += 1
            if d > 6:
                cd20 += 1
    break
while c != 0:
    if c < 5:
        cd50 += (c * 2)
    else:
        cd100 += c
    break
while m != 0:
    cd100 += (m * 10)
    break #fiquei com duvida porque tem um break aqui?
if cd1 != 0:
    print(f'{cd1} cédulas de 1,00')
if cd2 != 0:
    print(f'{cd2} cédulas de 2,00')
if cd5 != 0:
    print(f'{cd5} cédulas de 5,00')
if cd10 != 0:
    print(f'{cd10} cédulas de 10,00')
if cd20 != 0:
    print(f'{cd20} cédulas de 20,00')
if cd50 != 0:
    print(f'{cd50} cédulas de 50,00')
if cd100 != 0:
    print(f'{cd100} cédulas de 100,00')

l1 = float(input('lado a:'))
l2 = float(input('lado b:'))
l3 = float(input('lado b:'))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('é um triâgulo', end=' ')
    if l1 == l2 == l3:
        print('Equilátero')
    elif l1 != l2 != l3 != l1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('não é um triâgulo')

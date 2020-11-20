l1 = float(input('lado a:'))
l2 = float(input('lado b:'))
l3 = float(input('lado b:'))
if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('\033[4;33;44m é um triâgulo \033[m')
else:
    print('\033[7;37;41m não é um triâgulo \033[m ')

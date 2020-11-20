n1 = float(input('Primeiro Número: '))
n2 = float(input('Segundo Número: '))
m = (n1 + n2) / 2
if m >= 7:
    print('Aprovado')
elif m >= 5 and m < 7:
    print('Recuperação')
else:
    print('Reprovado')

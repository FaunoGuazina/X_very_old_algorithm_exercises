def leiaINT(text):
    x = str(input(text)).strip()
    while not x.isdigit():
        print('ERRO! só NUMERAL INTEIRO!')
        x = str(input(text)).strip()
    return int(x)


n = leiaINT('Digite um número: ')
print(f'vc digitou {n}')
num = int(input('digite um número: '))
print('''Escolha uma destas bases para conversão:
[1] para BINÁRIO
[2] para OCTAL
[3] para HEXADECIMAL''')
base = int(input('Base: '))
if base == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('base inexistente')

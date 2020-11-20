print('~'*30)
print('{:-^30}'.format(' TUPLAS Nº EXT '))
print('~'*30)
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Nº por extenso de 0 a 20: '))
    if 0 <= numero <= 20:
        print(f'O nº {numero} por extenso é {extenso[numero]}\n', '~' * 28)
    if numero < 0 or numero > 20:
        if numero == 69:
            break
        print('{:!^25}'.format(' Nº INVÁLIDO | 69 p/ SAIR '))

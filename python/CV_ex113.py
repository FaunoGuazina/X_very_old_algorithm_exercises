def leiaINT(text):
    while True:
        try:
            n = int(input(text))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! só NUMERAL INTEIRO!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mUSUÁRIO PAROU A BAGAÇA!\033[m')
            return 0
        else:
            return n


n = leiaINT('Digite um número: ')
print(f'vc digitou {n}')
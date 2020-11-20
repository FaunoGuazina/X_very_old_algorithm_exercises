from time import sleep


# def maior(*x):
#     print('=' * 30)
#     print(f'foram informados {len(x)} valores:')
#     for v in x:
#         print(v, end=' ')
#         sleep(.4)
#     print()
#     print(f'O maior valor foi {max(x)}')
#     sleep(1)
def maior(* num):  #solução GUANABARA para evitar erro em função vazia
    contador = maior = 0
    for i in num:
        if i > maior:
            maior = i
        contador += 1
        print(f'{i}', end=' ')
    print()
    if contador == 0:
        print('Não haviam números para serem analisados. ')
    else:
        print(f'Foram analisados {contador} números e o maior foi {maior}')
    print()

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

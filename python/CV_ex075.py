a = int(input('Digite um númeor:'))
b = int(input('Digite um númeor:'))
c = int(input('Digite um númeor:'))
d = int(input('Digite um númeor:'))
x = a, b, c, d
#ou poderia solicitar 4x o input em x = int(input('Digite um númeor:')), int(input('Digite um númeor:')), int(input('Digite um númeor:')), int(input('Digite um númeor:'))
print(x)
print(f'o valor 9 apareceu {x.count(9)} vezes')
if 3 in x:
    print(f'o número 3 aparece na {x.index(3)+1}ª posição')
elif 3 not in x:
    print('o número 3 aparece em nenhuma posição')# não precisa do f se não for formatar a string 
print('Os números pares são:', end=' ')
for par in x:
    if par % 2 == 0:
        print(par, end=' ')

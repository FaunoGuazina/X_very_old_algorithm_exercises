print('-+' * 20)
print(f'{"Lista Pares e Ímpares":^40}')
print('-+' * 20)
numeros = [[], []]
for n in range(1, 8):
    n = int(input(f'Digite o {n}º número: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('-+' * 20)
print(f'os valores pares digitados foram\n{sorted(numeros[0])}')
print(f'os valores ímpares digitados foram\n{sorted(numeros[1])}')

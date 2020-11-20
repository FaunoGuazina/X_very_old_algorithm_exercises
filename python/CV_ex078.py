valores = list()
for v in range(0, 5):
    valores.append(int(input(f'Digite o {v}º valor: ')))
print('~' * 50)
print(f'os valores digitados foram {valores}')
print(f'O maior valor foi {max(valores)} na posição: ', end='')
for p, v in enumerate(valores):
    if v is max(valores):
        print(p, end='... ')
print(f'\no menor valor foi {min(valores)} na posição: ', end='')
for p, v in enumerate(valores):
    if v is min(valores):
        print(p, end='... ')

'''SOLUÇÃO GUANABARA
       criou variaveis no começo: MAIOR = MENOR = 0
       usou for pra varrer a lista e verificar o maior e menor
'''
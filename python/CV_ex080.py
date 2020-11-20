valores = list()
# for v in range(0, 5):
#     v = int(input('Digite um valor: '))
#     valores.append(v)
#     if len(valores) == 1:
#         print('posição final')
#     elif valores[-1] <= valores[0]:
#         valores.pop()
#         valores.insert(0, v)
#         print('posição 0')
#     elif valores[-1] <= valores[1]:
#         valores.pop()
#         valores.insert(1, v)
#         print('posição 1')
#     elif valores[-1] <= valores[2]:
#         valores.pop()
#         valores.insert(2, v)
#         print('posição 2')
#     elif valores[-1] <= valores[3]:
#         valores.pop()
#         valores.insert(3, v)
#         print('posição 3')
#     else:
#         print('posição final')
# print(valores)

# SOLUÇÃO GUANABARA:
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n >= valores[-1]: #acrescentei = depois > para caso de repetição do número nõa entrar em posição anterior
        valores.append(n)
        print('posição final')
    else:
        position = 0
        while position < len(valores):
            if n <= valores[position]:
                valores.insert(position, n)
                print(f'adicionado na posição {position}')
                break
            position += 1
print(valores)

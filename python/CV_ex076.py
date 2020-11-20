produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.3, 'Livros', 34.9)
print('-'*30)
print(f'{"listagem de Preço":^30}')
print('-'*30)
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<21}R${produtos[p + 1]:>7.2f}')
print('-'*30)

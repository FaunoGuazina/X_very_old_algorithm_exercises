total = maismil = barato = qtd = 0
while True:
    produto = str(input('Nome: ')).strip().capitalize()
    preco = float(input('valor: €'))
    qtd += 1
    total += preco
    if qtd == 1 or preco < barato:
        barato = preco
        nomeb = produto
    if preco >= 1000:
        maismil += 1
    quest = ' '
    while quest not in 'SN':
        quest = str(input('Deseja continuar?')).strip().upper()[0]
    if quest in 'N':
        break
print(f'vc comprou {qtd} produtos num total de €{total:.2f}')
print(f'vc comprou {maismil} produtos acima de mil euros')
print(f'o produto mais barato custou {barato:.2f} e foi {nomeb}')

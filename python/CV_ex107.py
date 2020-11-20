from Guazina import ex107

valor = float(input('Digite um valor $: '))
print(f'A metade de {valor} é {ex107.moedaMETADE(valor)}')
print(f'O dobro de {valor} é {ex107.moedaDOBRO(valor)}')
print(f'Adicionando 10% a {valor} é {ex107.moedaAUMENTA(valor, 10)}')
print(f'Diminuindo 20% de {valor} é {ex107.moedaDIMINUI(valor, 20)}')

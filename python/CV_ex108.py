from Guazina import ex107, ex108

valor = float(input('Digite um valor $: '))
print(f'A metade de {ex108.formaEURO(valor)} é {ex108.formaEURO(ex107.moedaMETADE(valor))}')
print(f'O dobro de {ex108.formaEURO(valor)} é {ex108.formaEURO(ex107.moedaDOBRO(valor))}')
print(f'Adicionando 10% a {ex108.formaEURO(valor)} é {ex108.formaEURO(ex107.moedaAUMENTA(valor, 10))}')
print(f'Diminuindo 20% de {ex108.formaEURO(valor)} é {ex108.formaEURO(ex107.moedaDIMINUI(valor, 20))}')

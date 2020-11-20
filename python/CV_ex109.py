from Guazina import ex109, ex108

valor = float(input('Digite um valor $: '))
print(f'A metade de {ex108.formaEURO(valor)} é {ex109.METADE(valor, True)}')
print(f'O dobro de {ex108.formaEURO(valor)} é {ex109.DOBRO(valor, True)}')
print(f'Adicionando 10% a {ex108.formaEURO(valor)} é {ex109.AUMENTA(valor, 10, True)}')
print(f'Diminuindo 20% de {ex108.formaEURO(valor)} é {ex109.DIMINUI(valor, 20, True)}')

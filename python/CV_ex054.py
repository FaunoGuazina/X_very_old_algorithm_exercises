from datetime import date
hoje = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Ano de nascimento {}ª pessoa: '.format(pessoa)))
    idade = hoje - nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Temos {} pessoas maiores e {} menores de idade'.format(maior, menor))

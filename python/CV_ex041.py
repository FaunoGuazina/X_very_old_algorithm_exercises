from datetime import date
ano = int(input('Ano de nascimento: '))
hoje = int(date.today().year)
idade = hoje - ano
print('Neste ano vc completa {} anos'.format(idade))
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
elif idade <= 25:
    print('Categoria SENIOR')
else:
    print('Categoria MASTER')

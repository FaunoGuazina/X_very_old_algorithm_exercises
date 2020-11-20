somaidade = 0
maisidade = 0
maisvelho = ''
jovem20 = 0
for p in range(1, 5):
    print('{:-^20}'.format(' {}ª Pessoa '.format(p)))
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()
    somaidade += idade
    if sexo in 'Mm' and idade > maisidade:
        maisidade = idade
        maisvelho = nome
    if sexo in 'Ff' and idade <= 20:
        jovem20 += 1
print('A média das idades é {} anos'.format(somaidade/4))
print('o homem mais velho tem {} anos e se chama {}'.format(maisidade, maisvelho.title()))
print('neste grupo existem {} mulheres menores de idade'.format(jovem20))

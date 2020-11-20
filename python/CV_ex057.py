QuantPessoas = int(input('Quantas pessoas deseja cadastrar? '))
for p in range(1, QuantPessoas + 1):
    print('{:-^20}'.format(' {}ª Pessoa '.format(p)))
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo (M/F): ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Sexo (M/F): ')).strip().upper()[0]

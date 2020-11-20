maior18 = homens = mulherU20 = 0
while True:
    idade = int(input('Idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo[0] in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulherU20 += 1
    quest = str(input('Deseja continuar? ')).strip().upper()[0]
    while quest not in 'SN':
        quest = str(input('Deseja continuar? ')).strip().upper()[0]
    if quest == 'N':
        break
print(f'foram cadastrados:\n{maior18} pessoas maiores de 18 anos\n{homens} pessoas que do sexo masculino\n{mulherU20} mulheres menores de 20 anos')

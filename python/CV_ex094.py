print('==' * 20)
print(f'{"CADASTRO PESSOAS":^40}')
print('==' * 20)
cadastro = list()
totalidade = 0
while True:
    temp = dict()
    temp['Nome'] = str(input('Nome: ')).strip().title()
    temp['Idade'] = int(input('Idade: '))
    totalidade += temp['Idade']
    temp['Sexo'] = ' '
    while temp['Sexo'] not in 'FM':
        temp['Sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
    cadastro.append(temp)
    quest = ' '
    while quest not in 'SN':
        quest = str(input('CONTINUAR [S/N]? ')).strip().upper()[0]
    if quest == 'N':
        break
print('==' * 20)
mediaidade = totalidade / len(cadastro)
mulheres = list()
acimamedia = list()
for x in cadastro:
    if x['Sexo'] == 'F':
        mulheres.append(x['Nome'])
    if x['Idade'] > mediaidade:
        acimamedia.append(x)
print(f'O grupo tem {len(cadastro)} pessoas')
print(f'A média etária do grupo é {mediaidade}')
print(f'As mulheres cadastradas foram:\n{mulheres}')
print('Pessoas acima da média etária são:')
for x in acimamedia:
    print(x)
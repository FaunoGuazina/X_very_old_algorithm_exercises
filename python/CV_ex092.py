print('==' * 20)
print(f'{"CTPS":^40}')
print('==' * 20)
from datetime import date
cadastro = dict()
cadastro['Nome'] = str(input('Nome: ')).strip().title()
ano = int(input('Ano de nascimento: '))
cadastro['Idade'] = date.today().year - ano
cadastro['CTPS'] = str(input('CTPS: '))
if cadastro['CTPS'] != '':
    cadastro['Ano de Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = float(input('Qual salário: '))
    cadastro['Aposenta com'] = cadastro['Idade'] + 35 - (date.today().year - cadastro['Ano de Contratação'])
print('==' * 20)
for k, v in cadastro.items():
    if v == '':
        break
    if k == 'Aposenta com':
        print(f"{k}: {v}", 'Anos')
        break
    print(f"{k}: {v}")

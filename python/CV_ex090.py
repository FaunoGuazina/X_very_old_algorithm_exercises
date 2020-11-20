print('==' * 20)
print(f'{"Status Alunos":^40}')
print('==' * 20)
alunos = dict()
alunos['Nome'] = str(input('Nome do aluno(a): ')).strip()
alunos['Média'] = float(input(f"Média de {alunos['Nome']}: "))
if alunos['Média'] >= 7:
    alunos['Situação'] = 'Aprovado(a)'
elif alunos['Média'] >= 4:
    alunos['Situação'] = 'Recuperação'
else:
    alunos['Situação'] = 'Reprovado(a)'
print('==' * 20)
for k, v in alunos.items():
    print(f'{k}: {v}')
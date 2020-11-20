print('-+' * 20)
print(f'{"Cadastro de Pessoas/Pesos":^40}')
print('-+' * 20)
principal = list()
while True:  # Bloco de Indrodução dos dados das pessoas
    temp = list()
    temp.append(str(input('Nome: ').strip().title()))
    temp.append(int(input('Peso: ')))
    principal.append(temp[:])
    quest = ' '
    while quest[0] not in 'SN':
        quest = str(input('Continuar [S/N]? ')).strip().upper()[0]
    if quest == 'N':
        break
# ANÁLISE DE DADOS
Pesos = 0
for p in principal:
    Pesos += p[1]
media = Pesos/len(principal)
leves = list()
pesados = list()
for p in principal:
    if p[1] > media:
        pesados.append(p[0])
    elif p[1] < media:
        leves.append(p[0])
# IMPRESSÃO DE RESULTADOS
print('-+' * 20)
print(f'Foram cadastrados {len(principal)} pessoas')
print(f'A média de peso foi de {media}Kg')
print('A(s) pessoa(s) acima da média:')
print(pesados)
print('A(s) pessoa(s) abaixo da média:')
print(leves)

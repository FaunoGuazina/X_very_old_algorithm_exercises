print('-+' * 20)
print(f'{"Cadastro de Pessoas/Pesos":^40}')
print('-+' * 20)
galera = list()
dados = list()
totalpessoas = totalpesos = maispesado = maisleve = 0
acimamedia = list()
nome_maispesado = list()
abaixomedia = list()
nome_maisleve = list()
while True:  # Bloco de Indrodução dos dados das pessoas
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(int(input('Peso: ')))
    galera.append(dados[:])
    totalpesos += dados[1]
    dados.clear()
    totalpessoas += 1
    quest = ' '
    while quest[0] not in 'SN':
        quest = str(input('Continuar [S/N]? ')).strip().upper()[0]
    if quest == 'N':
        break
mediapesos = totalpesos / totalpessoas
for pessoas in range(0, len(galera)):  # Bloco de Definição do maior e menor peso
    if galera[pessoas][1] >= maispesado:
        maispesado = galera[pessoas][1]
    if galera[pessoas][1] <= maisleve or maisleve == 0:
        maisleve = galera[pessoas][1]
for pessoas in galera:  # Bloco de separação: pessoas acima/abaixo média & nomes dos +e- pesados
    if pessoas[1] > mediapesos:
        acimamedia.append(pessoas[0])
    else:
        abaixomedia.append(pessoas[0])
    if pessoas[1] == maispesado:
        nome_maispesado.append(pessoas[0])
    if pessoas[1] == maisleve:
        nome_maisleve.append(pessoas[0])
print('-+' * 20)
print('{:^40}'.format(f'Foram cadastradas {totalpessoas} pessoas'.upper()))
print(f'{f"A MÉDIA de peso foi {mediapesos:.1f}kg":^40}'.upper())
print(f'Pessoa(s) com peso ACIMA da média:\n| ', end='')
for pessoas in acimamedia:
    print(pessoas, end=' | ')
print()
print(f'Pessoa(s) com peso ABAIXO da média:\n| ', end='')
for pessoas in abaixomedia:
    print(pessoas, end=' | ')
print()
if len(nome_maispesado) == 1:
    print(f'A pessoa mais pesada é {nome_maispesado} com {maispesado}kg')
else:
    print(f'As pessoa mais pesadas são {nome_maispesado} com {maispesado}kg')
if len(nome_maisleve) == 1:
    print(f'A pessoa mais leve é {nome_maisleve} com {maisleve}kg')
else:
    print(f'As pessoas mais leves são {nome_maisleve} com {maisleve}kg')
print('-+' * 20)

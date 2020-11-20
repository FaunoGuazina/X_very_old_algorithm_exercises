valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    quest = ' '
    while quest[0] not in 'SN':
        quest = str(input('Continuar [S/N]? ')).strip().upper()
    if quest == 'N':
        break
print(f'Lista gerada = {sorted(valores)}')
valoresP = list()
valoresI = list()
for v in valores:
    if (v % 2) == 0:
        valoresP.append(v)
    else:
        valoresI.append(v)
print(f'Números pares = {valoresP}')
print(f'Números ímpares = {valoresI}')
# FICOU IGUAL DO GUANABARA, SÓ QUE ELE USOU FOR COM ENUMERATE

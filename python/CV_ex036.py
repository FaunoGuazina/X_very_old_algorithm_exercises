valor = float(input('valor do imóvel: '))
anos = int(input('tempo de pagamento em anos: '))
salario = float(input('valor do salário do solicitante: '))
meses = anos * 12
minimo = salario * 30 / 100
print('A quantidade de prestações seria de {} meses'.format(meses))
print('O valor da prestação seria de {:.2f}'.format(valor/meses))
if valor/meses < minimo:
    print('Financiamento pode ser APROVADO')
else:
    print('Valor da prestação excede valor mínimo')
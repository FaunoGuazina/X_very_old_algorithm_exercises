print('{:=^40}'.format(' PAGAMENTO '))
valor = float(input('Qual valor da compra: '))
print('''Escolha a forma de pagamento:
[1] A Vista em dinheiro
[2] Vencimento do cartão
[3] 2x no cartão
[4] +3x no cartão''')
forma = int(input('Forma de Pagamento? '))
if forma == 1:
    print('A VISTA: o valor com desconto é de {:.2f}'.format(valor - (valor * 10 / 100)))
elif forma == 2:
    print('VENCIMENTO: o valor com desconto é de {:.2f}'.format(valor - (valor * 5 / 100)))
elif forma == 3:
    print('2x CARTÃO: o valor total e com parcela de {:.2f}'.format(valor / 2))
elif forma == 4:
    parcela = int(input('Qual número de parcelas: '))
    print('{}x CARTÃO: o valor total é de {:.2f} e cada parcela de {:.2f}'.format(parcela, valor + parcela * (valor * 20 / 100), (valor / parcela + (valor * 20 / 100))))
else:
    print('opção invalida')

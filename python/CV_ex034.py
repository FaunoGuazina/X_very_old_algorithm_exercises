salario = float(input('qual o seu salário? '))
if salario <= 1500:
    print('seu novo salário será de {:.2f}'.format(salario + (salario*15/100)))
else:
    print('seu novo salário será de {:.2f}'.format(salario + (salario*10/100)))
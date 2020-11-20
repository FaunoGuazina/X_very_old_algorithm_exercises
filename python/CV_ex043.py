peso = float(input('Qual seu peso: '))
altura = float(input('Qual sua altura: '))
IMC = peso / (altura ** 2)
print('Seu IMC é {:.1f} e indica que está'.format(IMC), end=' ')
if IMC <= 18.5:
    print('abaixo do peso')
elif IMC <= 25:
    print('no peso ideal')
elif IMC <= 30:
    print('com sobrepeso')
elif IMC <= 40:
    print('obeso')
else:
    print('em obesidade mórbida')

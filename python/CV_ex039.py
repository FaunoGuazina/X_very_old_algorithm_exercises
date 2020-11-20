from datetime import date
ano = int(input('Ano de nascimento: '))
hoje = int(date.today().year)
idade = hoje - ano
print('Neste ano vc completa {} anos'.format(idade))
if idade > 18:
    print('Seu ano de alistamento foi {}'.format(hoje - (idade - 18)))
elif idade < 18:
    print('Seu ano de alistamento será {}'.format(hoje + (18 - idade)))
else:
    print('Fuja do país ou aliste-se já!')

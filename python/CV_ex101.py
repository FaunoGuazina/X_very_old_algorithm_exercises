def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if 65 > idade >= 16:
        return f'{idade} anos: VOTO OBRIGATÓRIO'
    elif idade > 65 or 16 <= idade < 18:
        return f'{idade} anos: VOTO FACULTATIVO'
    else:
        return f'{idade} anos: VOTO PROÍBIDO'


while True:
    ANO = int(input('Qual ano de nascimento: '))
    print(voto(ANO))
    print('~' * 25)
    quest = ' '
    while quest not in 'SN':
        quest = str(input('Continuar? ')).strip().upper()[0]
    if quest == 'N':
        break

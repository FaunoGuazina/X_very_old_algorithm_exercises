def leiaDINDIN():
    x = str(input('Digite um valor $: ')).strip()
    for c in x:
        if c == ',':
            c = '.'
    y = str.isnumeric(x)
    while y == False:
        print(f'ERRO! {x} não é um valor numérico')
        x = str(input('Digite um valor $: ')).strip()
        y = str.isdecimal(x)
        if y:
            return float(x)
    return float(x)
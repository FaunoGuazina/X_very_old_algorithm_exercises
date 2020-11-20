print('==' * 20)
print(f'{"FUNÇÃO TXT ADAPTÁVEL":^40}')
print('==' * 20)


def escreva(txt):
    x = str(txt).strip().title()
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(f'  {x}')
    print('~' * tamanho)


while True:
    texto = str(input('Digite o título: '))
    if texto == '':
        break
    escreva(texto)

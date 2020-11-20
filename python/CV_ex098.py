from time import sleep
def escreva(txt):
    x = str(txt).strip().capitalize()
    tamanho = len(txt) + 4
    print('~' * tamanho)
    print(f'  {x}  ')
    print('~' * tamanho)


def contagem(x, y, z):
    if z == 0:
        if x > y:
            z = -1
        else:
            z = 1
    if x > y and z > 0:
        z = -z
    if x > y:
        y -= 1
    if x < y and z < 0:
        z = -z
    if x < y:
        y += 1
    for c in range(x, y, z):
        print(c, end=' ')
        sleep(.3)
    print('FIM!')
    sleep(.3)


escreva('Contagem de 1 a 10 de 1 em 1:')
contagem(1, 10, 1)
escreva('Contagem de 10 a 0 de 2 em 2:')
contagem(10, 0, -2)
escreva('agora é sua vez:')
a = int(input('INÍCIO: '))
b = int(input('FINAL: '))
c = int(input('PASSO: '))
if c == 0:
    C = 1
elif c < 0:
    C = -c
elif c > 0:
    C = c
escreva(f'contagem de {a} a {b} de {C} em {C}')
contagem(a, b, c)

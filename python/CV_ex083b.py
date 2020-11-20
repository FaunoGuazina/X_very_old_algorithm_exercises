# GANABARA SOLUTIONS - nõa funciona com erros após sinal de igual
mat = str(input('expressão com parêntesis: '))
pilha = list()
for simbolo in mat:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão super válida!!!'.upper())
else:
    print('Expressão inválida!!!'.upper())

mat = str(input('expressão com parêntesis: '))
'''testes de expressões: (a*b)-)c(=12 _ ((a+b)*c = 2) _ ((a+b)*c) = (2+5) _ ()a+b)*c (= )(2+5)('''
parAa = list()
parFa = list()
parAb = list()
parFb = list()
if mat.count('(') == mat.count(')'):
    for p, v in enumerate(mat):
        if v == '(' and p < mat.index('='):
            parAa.append(p)
        elif v == ')' and p < mat.index('='):
            parFa.append(p)
        elif v == '(' and p > mat.index('='):
            parAb.append(p)
        elif v == ')' and p > mat.index('='):
            parFb.append(p)
    if len(parAa) == len(parFa) and len(parAb) == len(parFb):
        erroA = erroB = 0
        for x in range(0, len(parAa)):
            if parAa[x] > parFa[x]:
                erroA += 1
        for x in range(0, len(parAb)):
            if parAb[x] > parFb[x]:
                erroB += 1
        if erroA > 0 or erroB > 0:
            print('Expressão inválida!!!'.upper())
            print('Erro de parênteses')
            if erroA > 0:
                print('antes do igual')
            if erroA > 0 and erroB > 0:
                print('{:^15}'.format('&'))
            if erroB > 0:
                print('depois do igual')
        else:
            print('Expressão super válida!!!'.upper())
    else:
        print('Expressão inválida!!!'.upper())
        print('Esqueceu algun(s) parênteses')
else:
    print('Expressão inválida!!!'.upper())
    print('Esqueceu algun(s) parênteses')

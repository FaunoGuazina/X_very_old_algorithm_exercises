n1 = int(input('digite o 1º número'))
n2 = int(input('digite o 2º número'))
n3 = int(input('digite o 3º número'))
n = [n1, n2, n3]
n.sort()
print('o menor número é {}'.format(n[0]))
print('o maior número é {}'.format(n[-1]))

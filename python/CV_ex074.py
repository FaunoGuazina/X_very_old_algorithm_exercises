from random import randint
a = randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999), randint(0, 999)
print(f'os números são:\n{a}')
print(f'o maior número é {sorted(a)[0]}\no menor número é {sorted(a)[-1]}')
# poderia usar o método max(a) e min(a) para maior e menor.

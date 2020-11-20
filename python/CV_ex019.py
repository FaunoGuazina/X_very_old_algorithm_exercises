print('=ˆ= ' * 11)
print('           tria a l’atzar')
print('=ˆ= ' * 11)
from random import choice
alumnes = []
cicle = 0
while cicle < 5:
    alumnes.append(int(input('triar un nombre: ')))
    cicle = cicle + 1

print('el nombre triat va ser {}'.format(choice(alumnes)))

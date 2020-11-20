print('=ˆ= ' * 11)
print('           tria ordre a l’atzar')
print('=ˆ= ' * 11)
from random import shuffle
alumnes = []
cicle = 0
while cicle < 5:
    alumnes.append(int(input('triar un nombre: ')))
    cicle = cicle + 1
shuffle(alumnes)
print('l\'ordre triat va ser {}'.format(alumnes))

print('=ˆ= ' * 11)
print('         calculadora d’hipotenusa')
print('=ˆ= ' * 11)
import math  # importar só uma função > from math import hypot

co = float(input('longitud oposada a la cama: '))
ca = float(input('longitud de la cama contigua: '))
hip = math.hypot(co, ca)  # forma sem importação de biblioteca (co ** 2 + ca ** 2) ** (1/2)
print('la hipotenusa ha de mesurar {:.2f}'.format(hip))

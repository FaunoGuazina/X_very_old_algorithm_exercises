print('=ˆ= ' * 11)
print('           calculadora d\'angle')
print('=ˆ= ' * 11)
from math import radians, sin, cos, tan  # importar todo o módulo > import math

angle = float(input('introduir el valor d\'un angle: '))
sinus = sin(radians(angle))
cosinus = cos(radians(angle))
tangent = tan(radians(angle))
print('Si l\'ANGLE és {} el SINUS és {:.2f}\nel CONSINUS és {:.2f} i la TANGENT és {:.2f}'.format(angle, sinus, cosinus, tangent))

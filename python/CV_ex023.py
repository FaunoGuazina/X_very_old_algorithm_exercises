print('=ˆ= ' * 11)
print('             analitzant nombres')
print('=ˆ= ' * 11)
nom = int(input('introdueir un nombre? '))
u = nom // 1 % 10
d = nom // 10 % 10
c = nom // 100 % 10
m = nom // 1000 % 10
print('unitats = {}, desenes = {}, centenars = {}, milers = {}'.format(u, d, c, m))

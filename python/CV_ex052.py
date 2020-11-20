num = int(input('digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
print('de 1 até o numero {}, ele foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('por isso ele é primo')
else:
    print('por isso ele nõa é primo')
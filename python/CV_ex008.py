print('=ˆ= '*13)
print(' CONVERTER DE METRE EN CENTIMETRES I MIL·LIMETRES')
print('=ˆ= '*13)

metres = float(input('Introduïu una mesura en metres: '))
cm = metres * 100
mm = metres * 1000
print('La mesura {} en metres és igual a:\n{:.0f} centímetres i\n{:.0f} mil·límetres'.format(metres, cm, mm))

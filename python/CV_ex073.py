print('{:-^30}'.format(' TUPLAS COLOCAÇÕES'))
autonomos = ('Andaluzia', 'Catalunya', 'Madrid', 'Valencia', 'Galiza', 'Castela e Leão', 'País Basco', 'Canárias', 'Castilla-La Mancha', 'Múrcia', 'Aragão', 'Estremadura', 'Principado de Astúrias', 'Baleares', 'Navarra', 'Cantábria', 'La Rioja', 'Ceuta', 'Melilla')
print('As comunidades autonomas da Espanha são:'.upper())
print(autonomos)
print('=' * 30)
print('As 5 comunidades autonomas mais populosas são:'.upper())
for colocacão, populoso in enumerate(autonomos):
    if colocacão < 5:
        print(colocacão+1, populoso)
print('=' * 30)
print('As 4 comunidades autonomas menos populosas são:'.upper())
for colocacão, populoso in enumerate(autonomos[-4:]):
    if colocacão < 5:
        print(colocacão + 1, populoso)
print('=' * 30)
print('Listas das comunidades autonomas em ordem alfabética}'.upper())
print(sorted(autonomos))
print('=' * 30)
print(f'A Catalunya está na {autonomos.index("Catalunya")+1}ª posição de mais populosa')

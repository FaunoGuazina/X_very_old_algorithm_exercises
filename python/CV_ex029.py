velocitat = float(input('Quina velocitat conduïu: '))
if velocitat <= 80:
    print('Molt Bé, molt bé, conduir amb seguretat')
else:
    print('vas ser multat!!!')
    print('l’import de la multa és {:.2f}'.format((velocitat-80)*7))

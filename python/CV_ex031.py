distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    print('o custo da sua viagem é de {:.2f}'.format(distancia * 0.50))
else:
    print('o custo da sua viagem é de {:.2f}'.format(distancia * 0.45))

while True:
    tabuada = int(input('Digite valor da Tabuada: '))
    if tabuada <= 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} x {c:2} = {c * tabuada:3}')
    print('~' * 15)

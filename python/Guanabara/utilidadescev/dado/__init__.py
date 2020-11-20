def LEIADIN(msg):
    validade = False
    while not validade:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '' or entrada.isalnum():
            print(f'\033[0;31mERRO! "{entrada}" é um preço inválido!\033[m')
        else:
            validade = True
            return float(entrada)

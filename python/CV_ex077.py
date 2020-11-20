palavras = ('apreder', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'Na palavra {p.upper()} as vogais são:', end=' ')
    for i in p:
        if i.upper() in 'AEIOU':
            print(i.upper(), end=' ')
    print()

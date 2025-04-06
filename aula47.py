palavra_secreta = 'tamarindo'

digite_letra = input('Digite apenas uma letra')
pegando_inicial = digite_letra[0]


if pegando_inicial in palavra_secreta:
    print('Esta')
else:
    print('Nao')
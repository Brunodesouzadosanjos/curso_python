"""try:
    numero = int(input('Digite um numero inteiro: '))
    if numero%2 == 0:
        print('par')
    else:
        print('impar')
except:
    print('Isso não é um numero inteiro')"""
try:
    horario = int(input('Qual o horario? '))
    if horario <= 11 :
        print('bom dia')
    elif horario >= 12 and horario <= 17:
        print('boa tarde')
    else:
        print('Boa noite')
except:
    print('Informa apenas valores de 0 ate 23')
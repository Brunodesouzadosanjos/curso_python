nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome == '' or idade == 0:
    print('Digite algo')
else:
    print(f'seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    contar = len(' ' in nome)
    
    print(f'Seu nome contem {contar} de espaços')
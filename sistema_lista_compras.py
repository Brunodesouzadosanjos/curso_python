lista_compras = []
while True == True:
    opcao = input('deseja [i]nserir [a]pagar [l]istar  :  ')
    escolha = opcao[0].lower()
    if escolha == 'i':
        produto = input("produto: ")
        lista_compras.append(produto)
    elif escolha == 'a':
        print('apagar')
        produto = int(input('Digite o indice do produto para apagar: '))
        try:
            del lista_compras[produto]
        except:
            print('inexistente')

    elif escolha == 'l':
        for item in enumerate(lista_compras):
            indice,nome_produto = item
            print(indice, nome_produto)


    else:
        print('opção invalida')

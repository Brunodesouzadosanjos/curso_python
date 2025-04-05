op1 = input('Digite um numero: ')
op2 = input('Digite outro numero: ')

op1_1 = int(op1)
op2_2 = int(op2)
resultado = op1_1+op2_2

if op1_1 > op2_2:
    print(f'{op1_1} é maior que {op2_2}')
elif op1_1 < op2_2:
    print(f'{op1_1} é menor que {op2_2}')
else:
    print(f"{op1_1} é igual a {op2_2}")
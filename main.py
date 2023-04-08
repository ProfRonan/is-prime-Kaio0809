cont = 0
numero = int(input('Digite um número inteiro: '))
if numero < 0 or numero == 0:
    print('Número inválido')
else:
    for primos in range(1,numero+1):
        if (numero % primos) == 0:
            cont += 1
    if cont > 2 or numero == 1:
        print ('Não primo')
    else: 
        print('Primo')
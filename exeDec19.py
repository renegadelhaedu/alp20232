numero = int(input('digite um numero menor que 1000'))

if(numero >= 1 and numero < 1000):
    cent = numero // 100
    dez = (numero % 100) // 10
    uni = (numero % 10)

    if(cent > 1):
        print(f'{cent} centenas')
    else:
        print(f'{cent} centena')


else:
    print('numero invalido')
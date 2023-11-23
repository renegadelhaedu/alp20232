#numero primo, divisível só por 1 e por ele mesmo
quant = 0
for num in range(4, 10000):

    cont = 0

    for i in range(2, num):
        if(num % i == 0):
            cont = cont + 1

    if(cont == 0):
        quant = quant + 1
        print(f'o numero {num} eh primo')


#calculo do percentual de numeros primos contidos neste intervalo
print((quant/10000) * 100)
#numero primo, divisível só por 1 e por ele mesmo

num = 188
cont = 0

for i in range(2, num):
    if(num % i == 0):
        cont = cont + 1

if(cont == 0):
    print(f'o numero {num} eh primo')
else:
    print(f'o numero {num} NAO eh primo')
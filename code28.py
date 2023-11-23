#remove os numeros pares de uma lista
numeros = [0,1,2,3,4,5,6,7,8,9]

for i in numeros:
    if(i % 2 == 0 ):
        print(f'removi o numero {i}')
        numeros.remove(i)


print(numeros)

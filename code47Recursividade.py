def fatorial(num):
    if(num>1):
        num = num * fatorial(num - 1)
        return num
    else:
        return 1


def calcularSomatorioFunc(lista, i):
    # dados = [4,2,5]
    if (i == len(lista) - 1):
        soma = 3 * lista[i] + 5
        return soma
    else:
        soma = (3 * lista[i] + 5) + 31

    return soma

(3*4+5) + (3*2+5) + (3*5+5)


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib2(n):
    lista = [1,1]

    while (len(lista) < n):
        lista.append( lista[len(lista)-1] + lista[len(lista)-2] )
    return lista[len(lista)-1]


#dados = [4,2,5]
#print(calcularSomatorioFunc(dados, 0))

#print(fib2(3))

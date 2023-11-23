lista = [['rene','sousa',35],['jack','cz',25],['maria','sousa',58]]

remover = []
for i in range(len(lista)):

    for j in range(len(lista[i])):

        if(lista[i][j] == 'sousa'):
            remover.append(lista[i])

for elemento in remover:
    lista.remove(elemento)

print(lista)
print(remover)
del(remover)
print(remover)
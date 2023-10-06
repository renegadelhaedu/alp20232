numeros1 = [12,3,4,5,7,9,33]
numeros2 = [2,3,4,6,7,9,31]

inter = list()
disju = list()

for i in range(len(numeros2)):
    if (numeros2.count(numeros1[i]) == 0):
        disju.append(numeros1[i])

    if (numeros1.count(numeros2[i]) == 0):
        disju.append(numeros2[i])


for elementoLista1 in numeros1:
    #verificar se cada elemento da lista numeros1 está presente na lista numeros2
    if (numeros2.count(elementoLista1) > 0):
        #inserir o emento na lista de inter
        inter.append(elementoLista1)

print(f'inter: {inter}')
print(f'disju: {disju}')


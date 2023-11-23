alunos = {'rene': 4, 'jack': 2, 'maria': 3, 'lucas': 1}

lista_alunos = list(alunos.items())
print(lista_alunos)

n = len(lista_alunos)
for i in range(n):
    for j in range(0, n-1):
        if lista_alunos[j][1] < lista_alunos[j+1][1]:
            aux = lista_alunos[j]
            lista_alunos[j] = lista_alunos[j+1]
            lista_alunos[j + 1] = aux

print(lista_alunos)

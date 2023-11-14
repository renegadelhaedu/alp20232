alunos = {'rene': 13, 'jack': 7, 'maria': 19, 'lucas': 10}

lista_alunos = list(alunos.items())
print(lista_alunos)

n = len(lista_alunos)
for i in range(n):
    for j in range(0, n-i-1):
        if lista_alunos[j][1] < lista_alunos[j+1][1]:
            aux = lista_alunos[j]
            lista_alunos[j] = lista_alunos[j+1]
            lista_alunos[j + 1] = aux

print(lista_alunos)

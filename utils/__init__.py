def salvarArquivo(texto, caminho):
    f = open(f'{caminho}.txt', 'w')
    f.write(texto)
    f.close()


def gerarTextoSalvar(lista):
    texto = ''

    for item in lista:
        texto += item[0] + ' - ' + str(item[1]) + '\n'
    return texto

def ordenarDicionario(alunos):
    lista_alunos = list(alunos.items())
    print(lista_alunos)

    n = len(lista_alunos)
    for i in range(n):
        for j in range(0, n - 1):
            if lista_alunos[j][1] < lista_alunos[j + 1][1]:
                aux = lista_alunos[j]
                lista_alunos[j] = lista_alunos[j + 1]
                lista_alunos[j + 1] = aux

    return lista_alunos
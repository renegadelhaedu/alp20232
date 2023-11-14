#desenvolva uma solução
alunos = {'rene':13, 'jack':7, 'maria':19, 'lucas':10}
listaDec = []
maior = 0
for nome in alunos.keys():
    if(len(listaDec) == 0):
        listaDec.append(nome)
        print(listaDec)
    else:
        for j in range(len(listaDec)):
            if(alunos[nome] > alunos[listaDec[j]] ):
                listaDec.insert(j, nome)
                print(listaDec)

print(listaDec)







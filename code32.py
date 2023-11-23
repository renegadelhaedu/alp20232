alunos = list()
for i in range(2):
    nome = input('digite seu nome')
    corCamisa = input('digite a cor da sua camisa')

    alunos.append([nome, corCamisa])

print(alunos)

'''
contador = 0
for aluno in alunos:
    if(aluno[1] == 'branca' or aluno[1] == 'branco'):
        contador += 1

print(f'a quantidade de alunos de camisa branca é {contador}')
'''
contador = 0
for i in range(len(alunos)):
    if(alunos[i][1] == 'branca' or alunos[i][1] == 'branco'):
        contador += 1

print(f'a quantidade de alunos de camisa branca é {contador}')
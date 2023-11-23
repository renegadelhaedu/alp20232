#desenvolva um programa para ir lendo o nome dos alunos que estao em sala de aula e
# só pare quando for digitado a palavra fim. o programa deve ao final informar quantos alunos
#tem na aula

resposta = ''
cont = -1
while(resposta != 'fim'):
    resposta = input('digite seu nome')
    print(f'Seja bemvindo {resposta}')
    cont = cont + 1

print(f'hoje em sala tinham {cont} alunos')

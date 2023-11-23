#estruturas de dados = dicionário (chave:valor)
#nao utiliza índice
#dicionario nao aceita chaves duplicadas
#nao pode usar estruturas de dados como chave
lista = []
dicionario = {'renegadelha':['rene', 1234, 35,{1:'noticia1', 2:'noticia2'}],'maria55':['maria', 87654, 56]}

for i in range(3):
    login = input('digite seu login')

    while(True):
        contido = False
        for pessoa in dicionario:
            if(login == pessoa):
                contido = True
                break

        if(contido):
            print('login existente escolha outro')
            login = input('digite seu login')
        else:
            break

    senha = input('digite sua senha')
    nome = input('digite seu nome')
    idade = int(input('digite sua idade'))

    dicionario[login] = [nome, senha, idade]

    print(dicionario[login][1])

contador =0
for i in dicionario:
    if(dicionario[i][2] < 65):
        contador += 1




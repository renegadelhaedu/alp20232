#cria uma lista global que contenha previamente 3 nomes de login
# crie 1 def que receba como entrada a lista de logins e dentro leia um novo login
# de um usuário. só adicione na lista caso aquele login nao esteja contido.
#mostre uma mensagem informando se deu certo ou se já continha o login.

pessoas = ['clita','fabia','erica']

def inserirLista(lista):

    nome = input('digite seu nome')
    if nome in lista:
        print('já existe um login na lista')
    else:
        lista.append(nome)
        print('usuario inserido com sucesso')

inserirLista(pessoas)
print(pessoas)

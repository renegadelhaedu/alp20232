#percorra uma lista verificando se o usuario esta dentro da lista. retorne sim ou nao.

pessoas3 = ['matheus alves', 'cristofer', 'Dalina', 'Winicius','rian']

busca = input('digite o nome da pessoa que voce esta buscando')
achei = False
for pessoa in pessoas3:
    if(pessoa == busca):
        print(f'Sim. Encontrei {pessoa}')
        achei = True
        break

if(not achei):
    print('nao foi encontrado ninguem com esse nome')


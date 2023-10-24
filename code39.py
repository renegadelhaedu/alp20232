#escopo de uma variável GLOBAL X LOCAL
x = 1
def nadanada():
    print(x)
    return 'vai para los angeles'

def pi():
    return 3.14

def darboasvindas(kkk):
    print(f'seja bem-vindo {kkk}')

#essa funcao calcula a media de numeros passados por parametro em uma lista
def calcularmedia(nums):
    media = sum(nums) / len(nums)
    return media

def encontrarMenoresMedia(numeros):
    media = calcularmedia(numeros)
    novaLista = list()
    for i in numeros:
        if(i < media):
            novaLista.append(i)
    return novaLista

lista = [1,2,3,4,5,6,7,8,9]

menores = encontrarMenoresMedia(lista)


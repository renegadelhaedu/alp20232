carros = ['a','b','c','d','e']
premiados = []

for i in range(3):
    escolha = input('digite o nome do carro premiado')
    #verifica se a string carro está dentro da lista
    if(carros.count(escolha) > 0):
        #pega o indice do elemento na lista carros
        indice = carros.index(escolha)
        #inserir o elemento da lista carros na lista premiados
        premiados.append(carros[indice])
        #remover o elemento da lista carros
        carros.pop(indice)

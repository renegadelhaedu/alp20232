felipe = []


felipe.append({'maria': 32})
felipe.append({'carla':19})

soma = 0
for ficante in felipe:
    #soma += ficante.keys()
    for i in ficante.keys():
        print(ficante[i])
        soma += ficante[i]

media = soma / len(felipe)
print(media)

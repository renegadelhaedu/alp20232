nome = input('digite seu nome completo')
cont = 0
for i in nome:
    if(i  == ' '):
        cont = cont + 1

print(f'essa pessoa possui {cont + 1} nomes')
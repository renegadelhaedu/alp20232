users = [['renegadelha', 'renerene', 'rene de sousa'], ['jonintiktok', '12345', 'jonatas levi']]
login = 'renegadelha'
senha = 'carro'
logado = False
for lista in users:
    if (lista[0] == login and lista[1] == senha):
        logado = True

if (logado):
    print('voce esta logado no sistema')
    print('1-')

else:
    print('voce errou o login ou a senha')
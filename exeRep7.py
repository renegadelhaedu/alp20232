maior = 0
nome_maior = ''

for i in range(1, 6):
    num = int(input('digite um numero'))
    nome = input('digite seu nome')

    if(num > maior):
        maior = num
        nome_maior = nome

print('o maior numero lido foi ', maior)
print('digitado por ', nome_maior)


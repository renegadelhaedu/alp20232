num = input('digite um numero')
tam = len(num)
nova = ''

for i in range(tam -1, -1, -1):
    nova = nova + num[i]

print(nova)

'''
num = input('digite um numero')
tam = len(num)
nova = ''
while(tam > 0):
    nova = nova + num[tam - 1]
    tam = tam - 1

print(nova)

'''

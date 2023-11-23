import random as rd

cpf_user = ''
cpf = 13298746411
cont = 0
while(cpf_user != cpf):
    cpf_user = ''
    for i in range(11):
        digito = str(rd.randint(0,9))
        cpf_user = cpf_user + digito

    cont = cont + 1
    print(f'{cont} - gerou o CPF {cpf_user}')


print('achei o usuario do cpf')
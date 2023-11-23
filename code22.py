soma = 0
proxima = 'sim'

while(proxima == 'sim'):
    conta_dia = float(input('quanto foi o gasto de hoje'))
    soma = soma + conta_dia

    proxima = input('voce quer continuar comprando ou quer fechar a conta: sim/nao')

print(f'a conta parcial fechada foi R${soma}')


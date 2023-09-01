#operadores relacionais, quando usados, produzem como saída
#um valor booleano (True ou False)

idade = int(input('digite sua idade'))
if(idade >= 18):
    print('voce pode entrar na boate')
else:
    resta = 18 - idade
    print('voce vai ter que aguardar a maioridade')
    if(resta == 1):
        print(f'falta {resta} ano pois voce so tem {idade} anos')
    else:
        print(f'faltam {resta} anos pois voce so tem {idade} anos')


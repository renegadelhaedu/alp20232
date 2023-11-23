litros = float(input('digite a quantidade de combustivel'))
tipo = input('digite a-alcool ou g-gasolina')

if(tipo == 'a'):
    if(litros <= 20):
        total = (1.9 * litros) * 0.97
    else:
        total = (1.9 * litros) * 0.95
else:
    if (litros <= 20):
        total = (2.5 * litros) * 0.96
    else:
        total = (2.5 * litros) * 0.94

print(f'o valor final que sera pago e {total}')

kgmaca = float(input('digite quantos kilos de maca'))
kgmora = float(input('digite quantos kilos de morango'))

if(kgmora <= 5):
    valorMora = kgmora * 2.5
else:
    valorMora = kgmora * 2.2

if(kgmaca <= 5):
    valorMaca = kgmaca * 1.8
else:
    valorMaca = kgmaca * 1.5

if(kgmaca + kgmora > 8 or valorMaca + valorMora > 25):
    final = (valorMaca + valorMora) * 0.9
else:
    final = valorMaca + valorMora

print(f'o valor final a ser pago pelo cliente e {final}')


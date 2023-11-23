a = float(input('digite o valor de A'))

if(a == 0):
    print('nao é do segundo grau')
else:
    b = float(input('digite o valor de B'))
    c = float(input('digite o valor de C'))

    delta = b**2 - 4 * a * c

    if( delta > 0):
        x1 = (-b + delta ** (1/2)) / (2 * a)
        x2 = (-b - delta ** (1/2)) / (2 * a)
        print(x1)
        print(x2)
    elif(delta == 0):
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        print(x1)
    else:
        print('nao possui raizes reais')


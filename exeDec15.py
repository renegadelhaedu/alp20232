l1 = int(input('digite o lado do triangulo'))
l2 = int(input('digite o lado do triangulo'))
l3 = int(input('digite o lado do triangulo'))

if(l1 == l2 and l2 == l3):
    print('triangulo equilatero')
elif(l1 != l2 and l2 != l3 and l1 != l3):
    print('triangulo escaleno')
elif(l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l2 != l1):
    print('triangulo isosceles')

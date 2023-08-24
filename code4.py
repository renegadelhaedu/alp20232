#operadores aritmeticos

#s =s0 + v0T + att/2

#int()
#str()
#float()

s0 = float(input('digite o deslocamento inicial'))
v0 = float(input('digite a velocidade inicial'))
t = float(input('digite o tempo gasto'))
a = float(input('digite a aceleracao'))

s = s0 + v0 * t + (a*(t*t))/2

print('deslocamento final: ', s)


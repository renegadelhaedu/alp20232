sal = float(input('digite seu salario'))

if(sal <= 280):
    perc = 20
    aumento = sal * 0.20 #calculando o valor do incremento salarial
elif(sal <= 700):
    perc = 15
    aumento = sal * 0.15
elif(sal <= 1500):
    perc = 10
    aumento = sal * 0.10
else:
    perc = 5
    aumento = sal * 0.05


print(f'seu salario era R${sal} reais')
print(f'seu salario aumentou {perc}%')
print((f'seu salario foi aumentado em {aumento} reais'))
final = sal + aumento
print(f'seu salario final e R${final} reais')
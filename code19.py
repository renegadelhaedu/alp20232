#desenvolva um algoritmo em python que leia o salario bruto de 12 colaboradores
#o sistema deve retirar o imposto de acordo com a faixa do governo
#ao final, o sistema deve informar quanto de imposto foi arrecadado
# e qual o valor total dos salarios liquidos

total_impArrec = 0
total_salLiq = 0

for cont in range(1, 3):
    salario = float(input('digite seu salario bruto'))
    if(salario <= 2400):
        total_salLiq = total_salLiq + salario
        imposto = 0
    elif(salario <= 3200):
        imposto = salario * 0.075
        total_impArrec = total_impArrec + imposto
        total_salLiq = total_salLiq + (salario - imposto)
    elif(salario <= 4650):
        imposto = salario * 0.15
        total_impArrec = total_impArrec + imposto
        total_salLiq = total_salLiq + (salario - imposto)
    else:
        imposto = salario * 0.275
        total_impArrec = total_impArrec + imposto
        total_salLiq = total_salLiq + (salario - imposto)

    print(f'seu salario liquido ficou {salario - imposto}')

print(f'o total de salarios liquidos foi {total_salLiq}')
print(f'o total de imposto arrecadado foi {total_impArrec}')
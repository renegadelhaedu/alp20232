soma = 0
menor = 9999
maior = -9999
quantidade = 0

while(True):
    temp = float(input('digite a temperatura ambiente'))
    soma = soma + temp
    quantidade = quantidade + 1

    if(temp > maior):
        maior = temp

    if(temp < menor):
        menor = temp

    resp = input('voce quer continuar informando temperaturas sim/nao ?')
    if(resp == 'nao'):
        break

media = soma / quantidade
print(f'a media de temperaturas foi {media} graus')
print(f'a menor temperatura foi {menor} graus')
print(f'a maior temperatura foi {maior} graus')

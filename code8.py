peso = float(input('digite seu peso mas nao minta'))
altura = float(input('digite sua altura'))

imc = peso / (altura * altura)

if(imc > 30):
    print('chame o samu')
    perder = imc - 30
    print('voce precisa perder no IMC ', perder)
else:
    print('vc vai escapar vivo')

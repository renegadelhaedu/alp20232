#operadores lógicos

dinheiro = float(input('digite qnt dinheiro vc carrega'))
idade = int(input('diz ai tua idade'))
vestimenta = input('vc esta usando shorts ou calça?')

if(dinheiro >= 10 and idade >= 18 and vestimenta == 'calça'):
    print('pode entrar')
else:
    print('nao pode entrar')




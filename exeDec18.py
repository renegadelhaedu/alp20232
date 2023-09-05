dd = int(input('digite o dia do mês'))
mm = int(input('digite o mê do ano'))
aa = int(input('digite o ano'))

if(dd >= 1 and dd <= 31 and mm >= 1 and mm <= 12 and aa > 0):
    print('dia, mês e ano são válidos')
else:
    print('data inválida')
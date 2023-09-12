valor = 2
resto = valor

if(valor >= 100):
    c100 = valor // 100
    resto = valor % 100
    print(f'notas de 100:{c100}')
if(resto >= 50):
    c50 = resto // 50
    resto = resto % 50
    print(f'notas de 50:{c50}')
if(resto >= 10):
    c10 = resto // 10
    resto = resto % 10
    print(f'notas de 10:{c10}')
if(resto >= 5):
    c5 = resto // 5
    resto = resto % 5
    print(f'notas de 5:{c5}')
if(resto >= 1):
    c1 = resto // 1
    print(f'notas de 1:{c1}')

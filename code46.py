try:
    valor = float(input('digite a sua altura'))
    print(2/valor)
except:
    print('Tivemos um erro2')
    print(Exception.__cause__)
    print(Exception.__class__)

else:
    print(f'\nvalor lido: {valor}')

finally:
    print('boa sorte!')



'''
lista = [1,2,3,4]
itemRemover = int(input('digite um item para remover'))

try:
    x = lista.remove(itemRemover)

except:
    print('\no elemento nao existe na lista')

else:
    print('\nitem removido com sucesso')

finally:
    print('\noperacao concluida')
'''
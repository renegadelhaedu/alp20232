#mutável, ordenada pelo índice, sequencial
lista = list()

#par chave:valor, não é ordenado/sequencial, nao permite duplicidade das chaves
dicionario = dict()

#conjunto:  não é ordenado/sequencial, nao permite duplicidade
nomes = set()

import random

megasena = set()
while(len(megasena)!= 6):
    numero = random.randint(1,60)
    megasena.add(numero)

print(megasena)

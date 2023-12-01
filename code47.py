import utils

alunos = {'rene': 4, 'jack': 12, 'maria': 3, 'lucas': 1}

saida = utils.ordenarDicionario(alunos)
texto = utils.gerarTextoSalvar(saida)
utils.salvarArquivo(texto, '/home/rnsg/novoArquivo')

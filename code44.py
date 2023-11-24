news = {1:['rian eh o novo coordenador da catolica',
           'rian foi eleito pelos alunos e foi carregado nos bracos',['ele fraudou','ele merece']],
        2: ['asldaçslkdacatolica',
            'sekeiuytdfhgv carregado nos bracos', ['asjdhajsh', 'adas']]
        }

def salvarArquivo(texto, login):

    f = open(f'{login}.txt', 'a')
    f.write(texto)
    f.close()

textoSalvo = ''

for id in news.keys():
    textoSalvo += f'\ntitulo: {news[id][0]}\nConteudo: {news[id][1]}\n'
    textoSalvo += 'Comentarios\n'
    for comentario in news[id][2]:
        textoSalvo += f'\t--{comentario}\n'

salvarArquivo(textoSalvo, 'rene88')

#exercício 103 do curso de python do Curso em Vídeo
def ficha(gols, nome = 'desconhecido'):
    print('-' * 30)
    print('  NOME'.ljust(23, ' '), 'GOLS')
    print('  ', nome.ljust(21, ' '), gols)
    
jogador = str(input('digite o nome:'))
g = str(input('quantos gols ele fez?'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if jogador.strip() == '':
    ficha(gols=g)
else:
    ficha(g, jogador)
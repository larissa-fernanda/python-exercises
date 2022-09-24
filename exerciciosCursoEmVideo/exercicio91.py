#exercício 91 do curso de python do Curso em Vídeo
from random import randint
from time import sleep
from operator import itemgetter
aposta = {'jogador 1' : randint (1, 6),
        'jogador 2' : randint (1, 6),
        'jogador 3' : randint (1, 6),
        'jogador 4' : randint (1, 6)}
ranking = []
print('VALORES SORTEADOS'.center(30))
for k, v in aposta.items():
    print(f'O {k} tirou o valor {v}')
    sleep(1)
ranking = sorted(aposta.items(), key = itemgetter(1), reverse = True)
print('RANKING DOS JOGADORES:'.center(30))
for i, v in enumerate(ranking):
    print(f'  {i+1}o. lugar: {v[0]} com {v[1]}')
    sleep(1)
#exercício 88 do curso de python do Curso em Vídeo
from random import randint
from time import sleep
mega = []
jogos = int(input('quantos jogos deseja?'))
for tentativa in range (0, jogos):
    jogo = []
    for numero in range (0, 6):
        palpite = randint(1 , 60)
        if palpite not in jogo:
            jogo.append(palpite)
    jogo.sort()
    mega.append(jogo)
    
for n in range (0, jogos):
    print(f'Jogo {n+1}: {mega[n]}')
    sleep(1)

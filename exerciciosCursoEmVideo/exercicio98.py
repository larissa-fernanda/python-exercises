#exercício 98 do curso de python do Curso em Vídeo
from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        print('NÃO É POSSIVEL CONTAR DE 0 EM 0, CONTANDO DE 1 EM 1')
        passo = 1
    print('=' * 50)
    print(f'CONTAGEM DE {inicio} ATÉ {fim} DE {passo} EM {passo}:')
    contador = inicio
    if inicio < fim:
        while contador <= fim:
            print(contador, end = '...')
            contador += passo
            sleep(1)
    else:    
        while contador >= fim:
            print(contador, end = '...')
            contador -= passo
            sleep(1)
    print('FIM!')
    print('=' * 50)

contador(1, 10, 1)
contador(10, 0, 2)
print('SUA VEZ DE PERSONALIZAR A CONTAGEM:')
inicio = int(input('INÍCIO:'))
fim = int(input('FIM:'))
passo = int(input('PASSO:'))

contador(inicio, fim, passo)
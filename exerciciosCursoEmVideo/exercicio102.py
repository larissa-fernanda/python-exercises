#exercício 102 do curso de python do Curso em Vídeo
def fatorial(numero = 1, show = False):
    """
    Calcula o fatorial de um número:
        numero = numero a ser calculado (1 por padrao)
        show = se deve ser mostrado o processo (False por padrao)
    """
    print('-' * 30)
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    if show == True:
        for n in range (numero, 1, -1):
            print(f'{n} x', end = ' ')
        print(f'1 = ', end = ' ')
    if show == False:    
        return f
    return f

def fatorial_recursivo(numero):
    if numero <= 1:
        return numero
    
    return numero * fatorial_recursivo(numero - 1)
    
if __name__ == '__main__':
    numero = int(input('digite um numero:'))
    print(fatorial_recursivo(numero))
    print(fatorial(numero, False))


#exercício 97 do curso de python do Curso em Vídeo
def escreva(palavra):
    tamanho = len(palavra) + 4
    print('-' * tamanho)
    print(f'  {palavra}')
    print('-' * tamanho)
    
escreva('oi')
#exercício 96 do curso de python do Curso em Vídeo
largura = float(input('LARGURA (m):'))
comprimento = float(input('COMPRIMENTO (m):'))

def area(largura, comprimento):
    terreno = largura * comprimento
    print(f'A área de um terreno {largura:.2f}x{comprimento:.2f} é de {terreno:.2f}')

area(largura, comprimento)
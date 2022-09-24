#exercício 115 do curso de python do Curso em Vídeo
def leia_int(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido!')
            continue
        else:
            return numero

def linha(tamanho = 50):
    return '-' * tamanho

def cabecalho(mensagem):
    print(linha())
    print(mensagem.center(50))
    print(linha())
    
def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c}- {item}')
        c +=1
    print(linha())
    escolha = leia_int('Sua opção:')
    return escolha
#exercício 113 do curso de python do Curso em Vídeo
def leia_int(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido!')
            continue
        else:
            return numero

def leia_float(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido!')
            continue
        else:
            return numero

n = leia_int('digite um numero inteiro:')
print(f'voce acabou de digitar o numero {n}')
num = leia_float('digite um numero:')
print(f'voce acabou de digitar o numero {num}')

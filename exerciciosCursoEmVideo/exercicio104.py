#exercício 104 do curso de python do Curso em Vídeo
def leia_int(mensagem):
    ok = False
    valor = 0
    while True:
        n = str(input(mensagem))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('erro! digite um numero inteiro valido')
        if ok:
            break
    return valor
n = leia_int('digite um numero:')
print(f'voce acabou de digitar o numero {n}')
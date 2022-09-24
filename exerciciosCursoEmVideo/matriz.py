#exercícios 86 e 87 do curso de python do Curso em Vídeo
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceira_c = 0
maior_segunda_l = 0
for linha in range (0, 3):
    for coluna in range (0, 3):
        matriz [linha][coluna] = int(input(f'digite um valor para [{linha}, {coluna}]:'))
print('=' * 25)
print('       0   1   2' )
print()
for linha in range (0, 3):
    print(linha, end = '     ')
    for coluna in range (0, 3):
        print(f'[{matriz[linha][coluna]}]', end = ' ')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_terceira_c += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0 or matriz[1][coluna] > maior_segunda_l:
                maior_segunda_l = matriz[1][coluna]
    print()
print()
print('=' * 25)
print(f'a soma dos numeros pares é igual a {soma_pares}')
print(f'a soma dos valores da terceira coluna (2) é igual a {soma_terceira_c}')
print(f'o maior valor da segunda linha (1) é igual a {maior_segunda_l}')


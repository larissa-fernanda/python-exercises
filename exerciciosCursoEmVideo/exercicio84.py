#exercício 84 do curso de python do Curso em Vídeo
lista = []
while True:
    nome = str(input('digite seu nome:'))
    peso = float(input('digite seu peso:'))
    lista.append([nome, peso])
    perguntar = str(input('DESEJA CONTINUAR?'))
    if perguntar in 'Nn':
        break
lista.sort(key=lambda x: x[1])  
print(f'foram cadastradas {len(lista)} pessoas')
print(f'As pessoas mais leves têm {lista[0][1]}kg, ', end = '')
for pessoa in lista:
    if pessoa[1] == lista[0][1]:
        print(f'{pessoa[0]}', end = ', ')
print(f'enquanto as pessoas mais pesadas têm {lista[-1][1]}, ', end = '')
for pessoa in lista:
    if pessoa[1] == lista[-1][1]:
        print(f'{pessoa[0]}', end = ' e ')




    
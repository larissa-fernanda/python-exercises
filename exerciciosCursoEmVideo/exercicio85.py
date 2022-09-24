#exercício 85 do curso de python do Curso em Vídeo
lista = [[], []]
valor = 0
for c in range (1, 8):
    valor = int(input(f'digite o {c}o. valor:'))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
        
lista[0].sort()
lista[1].sort()

print(lista[0])
print(lista[1])
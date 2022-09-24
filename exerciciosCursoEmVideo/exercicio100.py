#exercício 100 do curso de python do Curso em Vídeo
from random import randint

def sorteia(lista, quantidade):
    for n in range (0, quantidade):
        lista.append(randint(1, 10 ))
    print(lista)

def soma_par(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos numeros pares é igual a {soma}')

numeros = []
sorteia(numeros, 10)
soma_par(numeros)
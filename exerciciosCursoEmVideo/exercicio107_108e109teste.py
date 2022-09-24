#exercícios 107,108 e 109 do curso de python do Curso em Vídeo
import exercicio107_108e109



preco = float(input('digite um valor: R$').replace(',','.'))
taxona = int(input('digite uma taxa de aumento:'))
taxinha = int(input('digite uma taxa de reduçao:'))
print(f'A metade de {exercicio107_108e109.moeda(preco)} é {exercicio107_108e109.metade(preco, formatacao = True)}')
print(f'O dobro de {exercicio107_108e109.moeda(preco)} é {exercicio107_108e109.dobro(preco, formatacao = True)}')
print(f'Aumentando {taxona}%, temos {exercicio107_108e109.aumentar(preco, taxona, formatacao = True)}')
print(f'Reduzindo {taxinha}%, temos {exercicio107_108e109.diminuir(preco, taxinha, formatacao = True)}')
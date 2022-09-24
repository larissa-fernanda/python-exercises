#exercícios 107,108 e 109 do curso de python do Curso em Vídeo
#107
def metade(numero = 0,  formatacao = False):
    meio = numero / 2
    if formatacao == False:
        return meio
    else:
        return moeda(meio)
    
def dobro(numero = 0, formatacao = False):
    dois = numero * 2
    if formatacao == False:
        return dois
    else:
        return moeda(dois)

def aumentar(numero = 0, taxa = 0, formatacao = False):
    aumento = numero * ((100 + taxa) / 100)
    if formatacao == False:
        return aumento
    else:
        return moeda(aumento)

def diminuir(numero = 0, taxa = 0, formatacao = False):
    reducao = numero * ((100 - taxa) / 100)
    if formatacao == False:
        return reducao
    else:
        return moeda(reducao)

#108
def moeda(numero = 0, moeda = 'R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')
#exercícios 107,108,109,110 e 112 do curso de python do Curso em Vídeo
#107
def metade(numero = 0,  formatacao = False):
    meio = numero / 2
    if formatacao == False:
        return meio
    #109
    else:
        return moeda(meio)
    
def dobro(numero = 0, formatacao = False):
    dois = numero * 2
    if formatacao == False:
        return dois
    #109
    else:
        return moeda(dois)

def aumentar(numero = 0, taxa = 0, formatacao = False):
    aumento = numero * ((100 + taxa) / 100)
    if formatacao == False:
        return aumento
    #109
    else:
        return moeda(aumento)

def diminuir(numero = 0, taxa = 0, formatacao = False):
    reducao = numero * ((100 - taxa) / 100)
    if formatacao == False:
        return reducao
    #109
    else:
        return moeda(reducao)

#108
def moeda(numero = 0, moeda = 'R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')
    
#110
def resumo(numero = 0, taxona = 10, taxinha = 5):
    print('-=' * 30)
    print('RESUMO DO VALOR'.center(60))
    print('-=' * 30)
    print(f'Preço analisado: \t{moeda(numero)}')
    print(f'Dobro do preço: \t{dobro(numero, True)}')
    print(f'Metade do preço: \t{metade(numero, True)}')
    print(f'Aumentando em {taxona}%: \t{aumentar(numero, taxona, True)}')
    print(f'Reduzindo em {taxinha}%: \t{diminuir(numero, taxinha, True)}')
    print('-=' * 30)

#112
def leia_dinheiro (mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem).replace(',','.')).strip()
        if entrada.isnumeric():
            valido = True
            return float(entrada)
        #if entrada.isalpha() or entrada == '':
        else:
            print(f'ERRO: \"{entrada}\" é um preço inválido!')    
            
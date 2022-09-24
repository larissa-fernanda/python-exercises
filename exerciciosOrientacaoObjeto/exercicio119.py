"""
Classe Retangulo: Crie uma classe que modele um retangulo:
    Atributos: LadoA, LadoB (ou Comprimento e Largura,
        ou Base e Altura, a escolher)
    Métodos: Mudar valor dos lados, Retornar valor dos
        lados, calcular Área e calcular Perímetro;
    Crie um programa que utilize esta classe: ele deve
        pedir ao usuário que informe as medidas de um local.
        Depois, deve criar um objeto com as medidas e calcular
        a quantidade de pisos e de rodapés necessárias para o local.
"""

class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_lados(self, comprimento_novo, largura_nova):
        self.comprimento = comprimento_novo
        self.largura = largura_nova

    def mostrar_lados(self):
        print('-' * 30)
        print(f'Comprimento: {self.comprimento}')
        print(f'Largura: {self.largura}')
        print('-' * 30)

    def area(self):
        Area = float(self.comprimento * self.largura)
        return Area

    def perimetro(self):
        Perimetro = float((2 * self.comprimento)+(2 * self.largura))
        return Perimetro

lugar_compr = float(input('qual o comprimento do local? '))
lugar_larg = float(input('qual a largura do local? '))
lugar = Retangulo(lugar_compr, lugar_larg)
area_lugar = lugar.area()
perimetro_lugar = lugar.perimetro()

piso_compr = float(input('qual o comprimento do piso? '))
piso_larg = float(input('qual a largura do piso? '))
piso = Retangulo(piso_compr, piso_larg)
area_piso = piso.area()
perimetro_piso = piso.perimetro()

rod_compr = float(input('qual o comprimento do rodapé? '))
rod_larg = float(input('qual a largura do rodapé? ' ))
rodape = Retangulo(rod_compr, rod_larg)
area_rodape = rodape.area()
perimetro_rodape = rodape.perimetro()

def quantidade_pisos(a_chao, a_placa):
    quantidade_placas = a_chao / a_placa
    return quantidade_placas

def quantidade_rodapes(p_chao, compr_plaquinha):
    quantidade_plaquinhas = p_chao / compr_plaquinha
    return quantidade_plaquinhas

print(f'Quantidade de pisos: {quantidade_pisos(area_lugar, area_piso)}')
print(f'Quantidade de rodapés: {quantidade_rodapes(perimetro_lugar, rodape.comprimento)}')

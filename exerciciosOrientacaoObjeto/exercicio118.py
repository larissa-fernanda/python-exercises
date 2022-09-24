"""
Classe Bola: Crie uma classe que modele uma bola:
    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor
"""
class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocar_cor(self, cor_nova):
        self.cor = cor_nova

    def mostrar_cor(self):
        print(self.cor)

bola = Bola('rosa', 20, 'borracha')
bola.mostrar_cor()
bola.trocar_cor('roxa')
bola.mostrar_cor()
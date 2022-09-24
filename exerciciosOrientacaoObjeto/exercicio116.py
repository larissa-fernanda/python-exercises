"""
Classe Quadrado: Crie uma classe que modele um quadrado:
    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área
"""

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudar_lado(self, lado_novo):
        self.lado = lado_novo

    def retornar_lado(self):
        print(self.lado)

    def area(self):
        ar = self.lado * self.lado
        return ar
    
    @property
    def aarea(self):
        ar = self.lado * self.lado
        return ar

quadrado = Quadrado(5)
quadrado.mudar_lado(4)
quadrado.retornar_lado()
print(quadrado.area())
print(quadrado.aarea)


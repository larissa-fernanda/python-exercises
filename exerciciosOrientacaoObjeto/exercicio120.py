"""
Classe Pessoa: Crie uma classe que modele uma pessoa:
    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer.
    Obs: Por padrão, a cada ano que nossa pessoa envelhece,
    sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        self.crescer(anos)

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kilos):
        self.peso -= kilos

    def crescer(self, tempo):
        if self.idade < 21:
            self.altura += tempo * 0.05

    def mostrar(self):
        print(f'Nome: {self.nome.title()}')
        print(f'Idade {self.idade} anos')
        print(f'Peso: {self.peso}kg')
        print(f'Altura: {self.altura}m')
        


pessoa = Pessoa('abc', 15, 70, 1.68)
pessoa.envelhecer(5)
pessoa.mostrar()
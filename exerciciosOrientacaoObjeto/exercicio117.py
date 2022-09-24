"""
Crie uma classe para representar uma pessoa,
    com os atributos privados de nome, 
    data de nascimento e altura. 
Crie os métodos públicos necessários para 
    sets e gets e também um método para 
    imprimir todos dados de uma pessoa. 
Crie um método para calcular a idade da pessoa.
A data de nascimento pode ser 
    informada como uma String 
    (no formato 05/10/1982, por exemplo) e, 
    no cálculo da idade, considere apenas o 
    ano da data de nascimento informada.
"""
from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, nascimento, altura):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__altura = altura
        self.anos()

    @property
    def nome(self):
        return self.__nome.title()

    @property
    def nascimento(self):
        return self.__nascimento

    @property
    def altura(self):
        return self.__altura

    def anos(self):
        ano_nascimento = int(self.nascimento.split('/')[-1])
        self.idade = self.ano_atual - ano_nascimento

    def imprimir(self):
        print(f'Nome: {self.nome}')
        print(f'Data de Nascimento: {self.nascimento}')
        print(f'Altura: {self.altura}')
        print(f'Idade: {self.idade}')

pessoa1 = Pessoa('fulaninho', '04/07/2000', 1.68)
pessoa1.imprimir()

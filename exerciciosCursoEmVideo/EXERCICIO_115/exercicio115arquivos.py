#exercício 115 do curso de python do Curso em Vídeo
from exercicio115 import *

def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
        
def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um erro na criaçao do arquivo!')
    else:
        print(f'arquivo {nome} criado com sucesso!')
        
def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado [1].replace('\n', '')
            print(f'{dado[0].ljust(20, " ")}{dado[1].rjust(3, " ")} anos')
    finally:
        a.close()
        
def cadastrar(arquivo, nome = 'desconhecido', idade = 0):
    try:
        a = open(arquivo, 'at+')
    except:
        print('houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houve um erro na hora de cadastrar os dados')
        else:
            print(f'novo registro de {nome} adicionado')
            a.close()


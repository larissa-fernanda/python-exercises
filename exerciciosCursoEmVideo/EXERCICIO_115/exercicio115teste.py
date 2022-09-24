#exercício 115 do curso de python do Curso em Vídeo
from exercicio115 import *
from exercicio115arquivos import *
from time import sleep

arquivo = 'abc.txt'

if not arquivo_existe(arquivo):
    criar_arquivo(arquivo)

cabecalho('SISTEMA DE CADASTRO DE PESSOAS')
while True:
    resposta = menu(['Listar Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        ler_arquivo(arquivo)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = int(input('Idade:'))
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('SAINDO DO SISTEMA... VOLTE SEMPRE!')
        break
    else:
        print('Opção inválida! Tente novamente!')
    sleep(1.5)
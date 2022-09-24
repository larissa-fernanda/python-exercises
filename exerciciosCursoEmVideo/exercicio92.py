#exercício 92 do curso de python do Curso em Vídeo
from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('DIGITE SEU NOME:'))
nascimento = int(input('SEU ANO DE NASCIMENTO:'))
cadastro['idade'] = datetime.now().year - nascimento
cadastro['ctps'] = int(input('DIGITE O No. DA CARTEIRA DE TRABALHO (0 = nao tem):'))
if cadastro['ctps'] != 0:
    cadastro['contratacao'] = int(input('QUAL O ANO DA SUA CONTRATAÇÃO?'))
    cadastro['salario'] = float(input('SEU SALÁRIO:'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratacao'] + 35) - datetime.now().year)
print('=-' * 20)
print('APOSENTADORIA'.center(30))
print('=-' * 20)

for k, v in cadastro.items():
    print(f' - {k} = {v}')
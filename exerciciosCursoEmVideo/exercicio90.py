#exercício 90 do curso de python do Curso em Vídeo
boletim = []
aluno = {}
perguntar = 's'
while perguntar not in 'Nn':
    aluno['nome'] = str(input('DIGITE O NOME:'))
    aluno['media'] = float(input('DIGITE A MÉDIA:'))
    if aluno['media'] >= 7:
        aluno['situacao'] = ' APROVADO'
    else:
        aluno['situacao'] = 'REPROVADO'
    boletim.append(aluno.copy())
    perguntar = str(input('DESEJA CONTINUAR? (n para parar)'))
boletim.sort(key=lambda x: x['nome'])
print('=-' * 20)
print('BOLETIM'.center(30))
print('=-' * 20)
print('No. ', 'NOME'.ljust(5, ' '), 'MÉDIA', 'SITUAÇÃO'.rjust(13, ' '))
for n in range (0, len(boletim)):
    print(n+1, '. ', boletim[n]['nome'].ljust(5,'.'), boletim[n]['media'], boletim[n]['situacao'].rjust(15, '_'))

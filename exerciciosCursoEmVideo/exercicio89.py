#exercício 89 do curso de python do Curso em Vídeo
boletim = []

class Aluno:
    def __init__(self, nome, nota_1, nota_2, media) -> None:
        self.nome = nome
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.media = media

perguntar = 's'
while perguntar not in 'Nn':
    media = 0
    nome = str(input('qual o nome?'))
    nota_1 = float(input('digite a 1 nota:'))
    nota_2 = float(input('digite a 2 nota:'))
    media = (nota_1 + nota_2) / 2
    aluno = Aluno(nome, nota_1, nota_2, media)
    perguntar = str(input('deseja continuar? (s/n)'))
    boletim.append(aluno)
boletim.sort(key=lambda x: x.nome)
print('=' * 30)
print(' ' * 11, 'BOLETIM')
print('=' * 30)
print('No. NOME', 'MÉDIA'.rjust(20, ' '))
for n in range (0, len(boletim)):
    print(n+1,'. ', boletim[n].nome.ljust(20, '.'),  boletim[n].media)
print('=' * 30)
individual = 's'
while individual not in 'Nn':
    individual = str(input('deseja ver as notas de algum aluno individual?'))
    if individual in 'Ss':
        quem = int(input('digite por favor numero do aluno:'))
        if quem <= len(boletim):
            print(f'PRIMEIRA NOTA: {boletim[quem-1].nota_1}')
            print(f'SEGUNDA NOTA: {boletim[quem-1].nota_2}')
        else:
            print('NÚMERO INVÁLIDO! TENTE NOVAMENTE')
print('=' * 30)
print('VOLTE SEMPRE!')
        
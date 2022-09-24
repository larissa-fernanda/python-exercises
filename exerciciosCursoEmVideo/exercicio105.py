#exercício 105 do curso de python do Curso em Vídeo
def notas(* n, situacao = False):
    """
    Função para analisar as notas e a situação de uma turma:
        n = notas dos alunos (aceita várias ou nenhuma)
        situacao = valor opcional, indicando se deve ou nao adicionar a situação da turma (boa, regular ou ruim)
        return = dicionario com as informações da turma
    """
    dicionario = {}
    dicionario ['total'] = len(n)
    if len(n) >= 1:
        dicionario ['maior'] = max(n)
        dicionario ['menor'] = min(n)
        media = sum(n) / len(n)
        dicionario ['media'] = media
    else:
        dicionario ['maior'] = dicionario ['menor'] = 0
        media = dicionario ['media'] = 0
    if situacao == True:
        if media >= 7:
            dicionario ['situacao'] = 'boa'
        elif media >= 5:
            dicionario ['situacao'] = 'regular'
        elif media < 5:
            dicionario ['situacao'] = 'ruim'
    return dicionario

print(notas(8, 9, 2, 5, situacao = True))
# help(notas)
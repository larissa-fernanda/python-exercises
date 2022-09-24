#exercício 101 do curso de python do Curso em Vídeo
def voto(nascimento):
    from datetime import datetime
    idade = datetime.now().year - nascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif idade >= 16 and idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

ano_nascimento = int(input('Em que ano você nasceu?'))
print(voto(ano_nascimento))
    
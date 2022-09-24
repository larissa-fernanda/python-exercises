#exercício 106 do curso de python do Curso em Vídeo
def ajuda(cmd):
    print('=-' * 50)
    help(cmd)

def titulo (mensagem):
    tamanho = len(mensagem) + 6
    print('=' * tamanho)
    print(f'   {mensagem}')
    print('=' * tamanho)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA DO PYTHON')
    comando = str(input('FUNÇÃO OU BIBLIOTECA: ["fim" para encerrar]'))
    if comando.lower() == 'fim':
        break
    else:
        ajuda(comando)
titulo('VOLTE SEMPRE!')
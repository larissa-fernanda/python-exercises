#exercícios 93 e 95 do curso de python do Curso em Vídeo
time = []
aproveitamento = dict()
while True:
    aproveitamento['nome'] = str.upper(input('digite o nome do jogador:'))
    partidas = int(input(f'quantos partidas {aproveitamento["nome"]} jogou?'))
    gols = []
    total = 0
    for n in range (0, partidas):
        partida = int(input(f'quantos gols ele fez na partida {n+1}?'))
        total += partida
        gols.append(partida)
    aproveitamento['gols'] = gols[:]
    aproveitamento['total'] = total
    time.append(aproveitamento.copy())
    while True:
        perguntar = str(input('DESEJA CONTINUAR? [S//N]')).upper()[0]
        if perguntar in 'SN':
            break
        print('ERRO! RESPONDA S OU N')
    if perguntar == 'N':
        break
print('=' * 50)
print('cód. ', end = '')
for i in aproveitamento.keys():
    print(f'{i:<15}', end = '')
print()
print('-' * 50)
for k, v in enumerate(time):
    print(f'{k:<3}.  ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
print('-' * 50)    
while True:
    busca = int(input('MOSTRAR DADOS DE QUAL JOGADOR? [999 PARA ENCERRAR]'))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! CÓDIGO INEXISTENTE')
    else:
        print(f'-> LEVANTAMENTOO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'Na partida {i+1}, ele fez {g} gols')
    print('=' * 50)
print('^_^ ^_^ VOLTE SEMPRE! ^_^ ^_^'.center(50))   
        

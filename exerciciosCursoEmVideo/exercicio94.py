#exercício 94 do curso de python do Curso em Vídeo
grupo = []
pessoa = {}
soma = media = 0
soma_f = contador_f = media_f = 0
soma_m = contador_m = media_m = 0
soma_i = contador_i = media_i = 0
while True:
    pessoa['nome'] = str(input('NOME:')).upper()
    while True:
        pessoa['sexo'] = str(input('SEXO: [M/F/I]')).upper()[0]
        if pessoa['sexo'] in 'MFI':
            break
        print('ERRO! TENTE NOVAMENTE!')
    pessoa['idade'] = int(input('IDADE:'))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        pergunta = str(input('QUER CONTINUAR? [S/N]')).upper()[0]
        if pergunta in 'SN':
            break
        print('ERRO! RESPONDA S OU N!')
    if pergunta == 'N':
        break
print('=-=' * 30)
print(f'Foram cadastradas {len(grupo)} pessoas.')
media = soma / len(grupo)
print(f'A média da idade de todas as pessoas cadastradas é {media:.2f}')
print('As pessoas do sexo feminino cadastradas foram: ', end = '')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end = '')
        soma_f += p['idade']
        contador_f += 1
    if p['sexo'] == 'M':
        soma_m += p['idade']
        contador_m += 1
    if p['sexo'] == 'I':
        soma_i += p['idade']
        contador_i += 1
print()
print('As pessoas que têm a idade acima da média do grupo: ', end = '')
for p in grupo:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end = '')
print()
media_f = soma_f / (contador_f or 1)
media_m = soma_m / (contador_m or 1)
media_i = soma_i / (contador_i or 1)
print(f'A média de idade das pessoas do sexo feminino cadastradas é {media_f:.2f}')
print(f'A média de idade das pessoas do sexo masculino cadastradas é {media_m:.2f}')
print(f'A média de idade das pessoas com sexo indefinido é {media_i:.2f}')
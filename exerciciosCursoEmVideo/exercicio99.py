#exercício 99 do curso de python do Curso em Vídeo
def maior(* numeros):
    if len(numeros) >= 1:
        print(f'Dentro dos valores {numeros}, o maior valor é {max(numeros)}')
    else:
        print(f'Em {numeros}, não há nenhum valor para ser analisado ')
    
maior(1,2,2,5,6,7)
#exercício 114 do curso de python do Curso em Vídeo
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://emcasa.com/')
except Exception as erro:
    print(f'deu erro {str(erro)}')
else:
    print('tudo ok')
    print(site.read())
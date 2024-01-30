import os

print(os.name)#função para mostrar seu sistema operacional


#verfica se arquivo existe
print(os.path.exists('texto.py'))
print(os.path.exists('22tuplas.py'))

#verifica se diretorio existe
print(os.path.exists('python'))
print(os.path.exists('novapasta'))

#verifica se arquivo existe atraves do caminho (quando dentro de outro diretorio)
print(os.path.exists('texto.txt'))
print(os.path.exists('novapasta/texto.txt'))

#criando arquivo
#os.mknod('olamundo.py')
#cria arquivo dentro  do diretorio atual, pq nao foi passado o nome da pasta

#OBS.: APÓS OS CODIGOS DE CRIAÇÃO DE ARQUIVOS E PASTAS SEREM EXECUTADOS PELA 1ª VEZ, É NECESSÁRIO COMENTAR A LINHA DO CÓDIGO, CASO CONTRÁRIO O PROGRAMA VAI APRESENTAR ERRO

#criando diretorio
#os.mkdir('python')

#os.mknod('/home/oem/Documentos/GitHub/python/python/python.py') #cria arquivo usando caminho absoluto

#os.mknod('./python/compras.txt')# cria arquivo usando caminho relativo atraves do (./)
#os.mknod('/python/compras02.txt')#apresenta erro pois falta o ponto(.)
#os.mknod('python/compras02.txt')#erro, pois nao ha (./)

#os.mkdir('./python/loja')#cria pasta loja dentro de pasta python --> (./) significa diretorio atual 
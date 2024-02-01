import os

print(os.name)#função para mostrar seu sistema operacional


#Verfica se arquivo existe
print(os.path.exists('texto.py'))
print(os.path.exists('22tuplas.py'))

#Verifica se diretorio existe
print(os.path.exists('python'))
print(os.path.exists('novapasta'))

#Verifica se arquivo existe atraves do caminho (quando dentro de outro diretorio)
print(os.path.exists('texto.txt'))
print(os.path.exists('novapasta/texto.txt'))

#Criando arquivo
#os.mknod('olamundo.py')
#cria arquivo dentro  do diretorio atual, pq nao foi passado o nome da pasta

#OBS.: APÓS OS CODIGOS DE CRIAÇÃO DE ARQUIVOS E PASTAS SEREM EXECUTADOS PELA 1ª VEZ, É NECESSÁRIO COMENTAR A LINHA DO CÓDIGO, CASO CONTRÁRIO O PROGRAMA VAI APRESENTAR ERRO

#Criando diretorio
#os.mkdir('python')

#os.mknod('/home/oem/Documentos/GitHub/python/python/python.py') #cria arquivo usando caminho absoluto

#os.mknod('./python/compras.txt')# cria arquivo usando caminho relativo atraves do (./)
#os.mknod('/python/compras02.txt')#apresenta erro pois falta o ponto(.)
#os.mknod('python/compras02.txt')#erro, pois nao ha (./)

#os.mkdir('./python/loja')#cria pasta loja dentro de pasta python --> (./) significa diretorio atual

#Apagando arquivos 
#os.remove('./python/compras.txt') -> arquivo fora do dir
#os.mknod('teste_para_apagar.py') -> arquivo criado dentro do dir
#os.remove('teste_para_apagar.py') -> arquivo foi apagado
print(os.path.exists('arquivo_para_remover'))#verificando se arquivo ainda existe
#os.remove('olamundo.py')

#Apagando diretórios
#os.remove('pastanova') #->não funciona com diretorios, exclusiva p/ arquivos
#os.rmdir('python')
#os.rmdir('pastanova') # deleta apenas diretórios vazios


#Renomeando arquivos e diretórios

#os.rename('python', 'novapasta')#renomeando a pasta 'python' para 'novapasta'
#os.rename('arquivo_para_renomear.txt', 'compras1.py')#é possivel modificar o nome e a extensão do arquivo

#os.rename('./novapasta/python.py', './novapasta/teste.py')#modificando usando o caminho relativo e deixando o arquivo dentro da mesma pasta. (caso nao passasse o caminho relativo no segundo parametro da função, o arquivo tete.py sairia de nova pasta e viria para o repositorio atual)
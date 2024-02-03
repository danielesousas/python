#PARA MANIPULAR ARQUIVOS DE TEXTO É PRECISO LOCALIZAR O ARQUIVO, ABRIR, ESCREVER E/OU LER E DEPOIS FECHÁ-LO, POIS SO SOs BLOQUEIAM QUAISQUER FUTURAR MODIFICAÇÕES EM UM ARQUIVO QUE JÁ ESTÁ ABERTO NO SISTEMA

#import os #para criar o arquivo .txt

#os.mknod('41leitura_e_escrita_de_arquivos.txt')
#arquivo = open('receita.txt')
#print(arquivo.closed)#verifica se o arquivo está aberto, caso esteja aberto pode-se ler e escrever nele
#print(arquivo.read())#função para ler o arquivo no terminal
#print(arquivo.read())#a receita nao é impressa novamente no terminal
#print(arquivo.closed)#verifica se o arquivo está fechado
#arquivo.close()#função para fechar o arquivo
#print(arquivo.closed)#verifica se está fechado novamente (dessa vez é True)

#print(arquivo.readline())#ler a primerira linha do arquivo
#print(arquivo.readline())#ler a segunda linha do arquivo, todos de forma agradável, a acentuação é bem legível também

#FORMA PYTHONIANA DE LER ARQUIVOS

with open('./novapasta/receita01.txt') as arquivo:#arquivo pode receber qualquer nome, como a, cadeira, balao...
    print(arquivo.closed)#arquivo aberto
    print(arquivo.read())#ler a receita dentro do terminal
    print(arquivo.closed)#arquivo aberto
print(arquivo.closed)#arquivo fechado

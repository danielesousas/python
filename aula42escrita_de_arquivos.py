#ESCRITA EM ARQUIVOS TXT EM PYTHON
"""
with open('./novapasta/receita01.txt') as arquivo:
    arquivo.write("Hello, world!")
    #dessa forma o codigo não funciona, pois está faltando um parâmetro de escrita ('w')
    """
""""
with open('./novapasta/receita01.txt', 'w') as arquivo:
    arquivo.write("Hello, world!")# A string sobrescreveu o que estava no arquivo

"""
var = """
I'm learning Python"""

with open('./novapasta/receita01.txt', 'a') as arquivo: #'a' de append, não vai sobrescrever o que está no arquivo, vai acrescentar a string no final do arquivo
    #arquivo.write("Hello, world!")
    arquivo.write(var)
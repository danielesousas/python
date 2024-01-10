#PARÂMETRO PADRÃO

#def imprimir_nome(nome="nome", sobrenome='sobrenome', idade='idade'):#parametro opcional
"""
def imprimir_nome(nome=None, sobrenome=None, idade=None):#parametro opcional
    if nome != None:
        print("Nome: ",nome)
        print("Sobrenome: ",sobrenome)
        print("idade: ",idade)
        print('-'*30)
    else:
        print("Por favor, insira seus dados.")



imprimir_nome()
imprimir_nome("dan", "iele", 25)
"""

def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None):
    print("-"*15)
    print('Nome: ',nomeImovel)
    print('Quantidade de quarts ', n_quartos)
    print('Vagas de Garagem: ', vagasGaragem)
    

# EXEMPLO DE Nº DE ARGUMENTOS <= Nº DE PARAMETROS
imprimir_imovel("Casa 3 Quartos - SP", 3)
imprimir_imovel("Studio 20", 1, 1)


#EXEMPLO DE Nº DE ARGUMENTOS >= Nº DE PARAMETROS
imprimir_imovel("Loja Comercial", 2, 1, "sale")#apresenta erro
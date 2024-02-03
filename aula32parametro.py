#parametros de uma fuunção
"""def minha_funcao():
    var= "ana"
    return var


#print(minha_funcao())
#var = "maria"
#print(var)
var = minha_funcao()
print(var)"""


"""
def nome_da_funcao(parametro):#parametro é o nome dado aos valores usados na definicao de uma funçao
    print("Olá", parametro)

nome = input("Qual seu nome? ")
nome_da_funcao(nome)# ->usando parametros nao necessario o mesmo nome na funcao 


print("-"*30)"""

def imprime_nome(parametro_nao_precisa_ter_o_mesmo_nome_da_variavel):
    print("hello, ", parametro_nao_precisa_ter_o_mesmo_nome_da_variavel)


nome = input("Qual seu nome? ")
imprime_nome(nome)
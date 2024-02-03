#Argumento Arbitrário **Kwargs - Keyword Arguments
#Essa função recebe argumentos que serão atribuidss em um dicionário
#Usado quando não se sabe quandos argumentos nomeados serão passados


def imprimir_nomes(**nomes):
    print(f"{nomes['nome']} {nomes['sobrenome']}")


imprimir_nomes(nome='ana', sobrenome='maria')

""""
def imprimir_nomes(nomes):
    print(f"{nomes['nome']} {nomes['sobrenome']}")


dicio = {'nome': 'dan', 'sobrenome': 'iele'}
imprimir_nomes(dicio)"""
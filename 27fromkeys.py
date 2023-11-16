tupla = ("item1", "item2", "item3")

"""
x= 0
dicio = dict.fromkeys(tupla, x)#passando o parametro x todos os itens recebem o valor atribuido a ele 
print(dicio)#cria um dicionario a partir da tupla
"""
"""
tupla2 = ("item1", "item2", "item3")
dicio = dict.fromkeys(tupla,tupla2)
print(dicio)#atribui uma tupla p/ cada item
"""
#ANINHAMENTO DE DICIONARIOS
dicio = {
    "dicio1" : {#o valor do dicionario é um dicionario (dicionario dentro de dicionario)
        "nome" : "Dan",
        "idade" : 27
    },
    "dicio2" : {
        "nome" : "Pedro",
        "idade" : 35,
        "dicio3" : {#dicionario dentro de dicionario e dentro de outro dicionario
            "nome" : "Mary Jane",
            "idade" : 2
        }
    }
}
print(dicio)

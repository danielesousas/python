"""

lista = ["car", "boat", "airplane"]
print(lista)

for x in range(len(lista)):
    print(x, lista[x])

texto = "car, airplane"
lista2 = list(texto)
print(lista2)

texto = texto.split(',')#p/ a virgula nao ser adicionada a lista 
#a string vai ser adicionada sem separacao de cada indice de letra, cada string sera um novo item
print(texto)
"""


lista = ["car", "boat", "airplane"]
print(lista)

"""
lista.append("moto",)#adiciona item ao final a lista, so aceita um argumento (mais de um apresenta error)
print(lista)

lista.append(["bike", "skate"])#um index recebeu uma lista (uma lista pode conter outra lista)
print(lista)

for x in range(len(lista)):
    print(x, lista[x])
"""

lista.insert(1, "bike")#adiciona barco no item 1, porem barco nao some
print(lista)

for x in range(len(lista)):
    print(x, lista[x])

lista.extend(["bike", "jetski"])#acrescenta mais de um elemento separadamente
print(lista)

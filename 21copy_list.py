"""

lista = ['a', 'b', 'c']
lista2 = [1, 4, 7]

lista = lista + lista2
print(lista)

lista.extend(lista2)#coloca alista dentro da outra (concatenação)
print(lista)

for x in lista2:
    lista.append(x)

print(lista)"""


"""
lista = ['a', 'b', 'c']
print(lista)

lista2 = lista
print(lista)

lista2.append('d')#o index é adicionado as duas listas
lista.append('e')

print(lista)
print(lista2)"""

lista = ['a', 'b', 'c']
print(lista)

lista2 =lista.copy()#c/ a funcao copy as lista sao modificadas separamente
print(lista2)

lista2.append("d")
lista.append('e')

print(lista)
print(lista2)
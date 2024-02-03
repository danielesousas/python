#SETS: coleção não-ordenada, imutável e que nao permite valores duplicados (tambem são conhecidos como conjuntos)


"""conjunto = {"item1", 'item2', "item3", "item3", "item2", "item1", True, 9.7, 500}#nao é feita nenhuma referencia atraves do index
print(conjunto)
print(type(conjunto))
print(len(conjunto))"""



tupla = (3, 7, 9, 5)
conjunto = set(tupla)
print(conjunto)
print(type(conjunto))

for x in conjunto:
    print(x)

print(9 in conjunto)
print(2 in conjunto)

#adicionar itens ao set
conjunto.add("adicionar item")
print(conjunto)


set1 = {4, 5, 7 , 12, 1.2 }
set2 = {"item1", "item2", "item3"}
set1.update(set2)
print(set1)

set1.update([100, 12, 5, "item1", "ADS"])
print(set1)

#Remover itens do set
set1.pop()
print(set1)

set1.remove("item3")#tentar remover item q nao existe, apresenta erro
set1.discard("item2")#tentar remover item q nao exite, NÃO apresenta erro
print(set1)

set1.clear()
print(set1)

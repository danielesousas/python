tupla1 = ("item1",)
tupla2 = ("a", "b")

tupla3 = tupla1 + tupla2
print(tupla3)

tupla4 = tupla1 * 3
print(tupla4) 

for x in tupla4:
    print(x)

for x in range(len(tupla4)):
    print(x, tupla4[x])

#DESEMPACOTAR TUPLA 

(x, y, z) = tupla4
print("x: ",x)
print("y: ",y)
print("z: ",z)

(x, *y) = tupla4 #c/ o asterisco a variavel y recebeu dois itens
print("x: ",x)
print("y: ",y)

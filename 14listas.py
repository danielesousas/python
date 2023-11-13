lista = ["python", "java", "cobol"]

print(lista)

lista2 = [2, 10, 2000, 25]
print(lista2)

lista3 = [2.3, 9.9, 10.0, 7.5]
print(lista3)

#for x in lista:
#   print(x, end="$")

lista4 = [True, False]
print(lista4)

lista5 = [True, "dan", 9.9, 10, "ADS"]
print(lista5)

print(type(lista5))

#SLICING -> selecionando indices

print(lista2[2])#imprimindo dado especifico da lista

print(lista5[-2])#item na ordem oposta

print(lista5[::])#imprime tudo do array do comeco ao fim
print(lista5[1:])#imprime do index 1 até o fim dp array
print(lista5[2:])
print(lista5[:3])#imprime do comeco do array ate o index 3-1
print(lista5[1:4])#comeca no index 1 e vai ate o index 4-1
print(lista5[1:4:2])#inicia do index 1, vai ate o index 4-1, de dois em dois itens

nome = "daniele"

print(nome[::])#slicing funciona com strings tambem


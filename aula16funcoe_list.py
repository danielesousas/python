nome = "Curso de Python"
valor = range(10)

print(nome)
print(valor)

#TRANSFORMANDO RANGE EM LISTA

lista = list(range(10))
print(lista)

#TRANSFORMANDO STRING EM LISTA

lista2 = list("Curso de Python")
print(lista2)

elemento = 18

if elemento in lista:
    print("O elemento esta na lista")
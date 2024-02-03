lista = ["cat", "dog", "fish", "shark", "eagle"]
print(lista)



lista[1] = "horse"#troca o item da lista
print(lista)

lista[1:4] = ["elephant", "monkey", "spider"]
print(lista)#mudando varios itens usando slicing

lista[1:2] = ["eagle", "bull", "pinguin"]
print(lista)#quando se itens a mais que o valor de index indicado no spicing(no caso seria apenas 1), foi acrescentado index

print(lista[1])
print(lista[2])
print(lista[3])

lista[1:5] = ["buffalo"]
print(lista)#qunado o numero de itens é menor que o slicing se perde indices
print(len(lista))


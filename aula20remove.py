lista = ["car", "bike", "skate"]
print(lista)

"""
lista.pop()#remove o ultimo item lista

lista.pop(0)#remove item no index 0

for x in range(len(lista)):
    print(x, lista[x])

"""

#del lista#a lista foi deletada, gerando o erro

del lista[1]#deleta o item do index 0
print(lista)

carrinho_compras = ["item1", "item2","item3"]
carrinho_compras.clear()#apaga os elementos, mas o array permanece existindo

print(carrinho_compras)

carrinho_compras2 = ["bread", "cookies", "milk"]
carrinho_compras2.sort()#coloca os itens em ordem alfabetica
print(carrinho_compras2)

listanum = [1, 43, 32, 101, 75]
print(listanum)

listanum.sort()#coloca os numero em ordem crescentes
print(listanum)

"""sort coloca em ordem alfabetica strings iniciadas em letra maiusculas e depois em letras minusculas"""


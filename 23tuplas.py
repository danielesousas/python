tupla = ("item1", "item2")
print(tupla)

tupla = ("item3", "item4", "bluedragon" )
print(tupla)

#nao apresenta erro pq aqui esta criando outra tupla com o mesmo nome da anterior

estados_brasil =("CE", "DE", "SP", "RN")#dessa forma nao é possivel adiciionar ou remover elementos, é imutavel
print(type(estados_brasil))

tupla1 = ("item1")#tupla c/ um so index é uma string
print(tupla1)
print(type(tupla1))

#p/ tranforma-la em tupla é necessario por uma virgula apos as aspas

tupla2 = ("item1",)
print(tupla2)
print(type(tupla2))

#o que faz uma tupla ser uma tupla é a VÍRGULA, nao os parenteses

tupla3 = "item1", "item2", "item3"
print(tupla3)
print(type(tupla3))

#transformando tupla em lista
tupla4 = ("cobol", "java", "ruby")
lista = list(tupla4)
print(tupla4)
print(type(tupla4))
print(lista)
print(type(lista))

lista.append("csharp")

#transformando lista em tupla novamente

tupla4 = tuple(lista)
print(tupla4)

del tupla4
print(tupla4)



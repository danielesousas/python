


dicio = {"nome" : "Dan", "ano" : 2000, "valor_logico" : True}
print(dicio)

dicio["nome"] = "Pedro"#mudando valr da chave
print(dicio)

dicio["idade"] = 30 #acrescenta chave ao dicionario 
print(dicio)

dicio.update({"nome": "ana"})#funcao update so funciona c/ dicionarios
print(dicio)

dicio.update({"estado" : "SP"})#acrescentando chave que nao exite, isandi funcao update
print(dicio)

dicio.popitem()#elimina o ultimo item do dicionario
print(dicio)

dicio.pop("valor_logico")
print(dicio)#elimina a chave selecionada

del dicio["ano"]
print(dicio)

#del dicio
#print(dicio) colocando esse codigo, o programa apresenta erro pois ele  nao esta mais definido

#dicio.clear()#apaga todos os dados do dicionario, porem nao o apaga, fica um dicionario vazio
print(dicio)

for x in dicio:
    #print(x) assim ele exibe apenas as chaves
    print(dicio[x])#assim ele exibe os valores das chaves

for x in dicio.values():#exibe todos os valores tambem
    print(x)

for x in dicio.items():
    print(x)#exibe as tuplas

for x, y in dicio.items():#exibe a chave e o valor
    print(x, y)

dados = dicio.copy()#copiando dicionario
print(dados)

dicio2 = dict(dados) #transforma variavel em dicionario a partir de um outro dicionario
print(dicio2)

dados["idade"] = 27
print(dados)
print(dicio)
print(dicio2)

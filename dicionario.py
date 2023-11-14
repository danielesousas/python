#DICIONÁRIO: coleção não-ordenada, mutável e que não permite valores duplicados

#chave:valor
#a chave nao pode ser duplicada
dicio = {"chave1" : "Dan", "chave2" : 1999, "chave3" : True }
print(dicio)

dicio_com_quebra_de_linha = {
    "nome": "maria",
    "idade": 15,
    "Brasil": True
}
print(dicio_com_quebra_de_linha)

print(dicio_com_quebra_de_linha['idade'])#acessa chave do dicionario

print(dicio_com_quebra_de_linha.get('idade'))#acessa chave c/ funcao GET

print(dicio.keys())#imprime todas as chaves do dicionario
print(len(dicio))
print(dicio_com_quebra_de_linha.values())#imprime os valores das chaves

if "idade" in dicio_com_quebra_de_linha:
    print("A chave idade existe")

print(dicio_com_quebra_de_linha.items())
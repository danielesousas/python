#O ARGUMENTO ARBITRÁRIO *ARGSS

def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None, *args):#o args desconsidera qualquer valor a mais que o usuario inserir no sistema
    print("-"*15)
    print('Nome: ',nomeImovel)
    print('Quantidade de quarts ', n_quartos)
    if vagasGaragem != None:
        print('Vagas de Garagem: ', vagasGaragem)
    print('Telefones: ', *args)#caso nao ponha o print, ele desconsidera os valores a mais sem gerar erro no codigo

imprimir_imovel("Loja Comercial", 3, 2, "11 99999-9999", "88 99999-9999")


def imprimir_nome(*nomes):
    print(nomes)


lista = ['ana', 'beatriz', 'hianna']
print(*lista)#ao usar o *, os itens da tupla sao desempacotados
print(type(lista))
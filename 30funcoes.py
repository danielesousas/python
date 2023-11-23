#Paradigma imperativo -> executa sequencias

#variaveis, atribuicoes e sequencia

nome = "daniele"#variavel global


def my_function():

    nome = "maria"#variavel local
    print(nome)#chama a variavel local, caso a indentacao volte pra tras, vai chamar a variavel global

print(nome)
my_function()

print(nome)

def imprime_tudo():
    nome = "funcao funcionando"
    tupla = (2, 4, 6, 1)
    print(nome)
    print(tupla)
    if nome == "funcao funcionando":
        print(f"Impressão do nome é igual a {nome}")
    for x in tupla:
        print(x)

imprime_tudo()
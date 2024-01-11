#Descobrindo se numero são primos

def numeroPrimo(numero):
    numero = int(input("Insira um número para descobrir se o mesmo é primo"))

    if numero > 1:
        for x in range(2, numero):
            if (numero % x) == 0:
                 return "Não é primo"#a palavra chave return faz a esma coisa que o break
        else:
                return "Esse número é primo"
    else:
        return "Esse número não é primo"


numeroPrimo()
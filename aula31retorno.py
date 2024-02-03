"""def ola_mundo():
    print("ola, mundo!")
    return True

retorno = ola_mundo()
print(retorno)

print(ola_mundo())"""


"""def par_impar():
    pass

#uma funcao vazia apresenta erro, porem com o pass nao ha erros


par_impar()"""

def par_impar():
    num = 21
    if(num % 2) == 0:
        return "numero par"
    return "numero impar"


print(par_impar())

x = 3
if x == 0:
    print("0")
print("ola")
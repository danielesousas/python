#Descobrir se numero é ímpar ou pr 

numero = int(input("Insira um numero para saber se o mesmo é par ou ímpar: "))
if(numero)% 2 == 0:
    print(f"{numero} é par")
else:
    print(f"{numero} é ímpar")

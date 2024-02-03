#Como encontrar o fatorial de um número
fatorial = 1

numero = int(input("Insira um número: "))

if numero < 0:
    print("Não existe fatorial de números negativos")
elif numero == 0:
    print("O fatorial de zero é igual a 1")
else:
    for x in range(1, numero + 1):
        fatorial *= x
    print(f"o fatorial de {numero} é: {fatorial}")


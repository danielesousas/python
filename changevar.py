#troca de variaveis em python

x = input("Insira o valor de x: ")

y = input("Digite o valo de y: ")

temp = x
x = y
y = temp

print(f"O valor de x depois da troca: {x}")
print(f"O valor de y depois da troca: {y}")
print(f"O valor de temp depois da troca: {temp}")
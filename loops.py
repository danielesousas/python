#LOOPS

#while
""""
a = 0

while a <= 5:
    print(a<=5)
    print(a)
    a +=  1


print('Resultado final de a:', a)
"""

#break 
"""
a = 0
while a <= 5:
    print(a <= 5)
    print(a)
    if a == 3:
        break
    a = a + 1

    print("Resultado final de a: ",a)
    print(a <=5)
"""
"""
#else


a = 0

while a <= 5:
    print(a <= 5)
    print(a)
    a += 1 

else:
    print(f" não é iguaç a 5. Valor de a: {a}")
"""


"""
s = "ceara"

for x in s:
    print(x)
"""
"""
for x in range(999): #range
    print(x)


for x in range(5,5):
    print(x)
"""
"""
for x in range(0, 6, 1): #terceiro parametro é o passo (vai ler os numeros de um em um, caso for dois leria de dois em dois e assim por diante )
    print(x)
"""

for x in range(6): # mesma coisa de -> for(x=0;x<=5;x++) em outras linguagens de programação
    print(x)
else:
    print("Chegamos ao fim")
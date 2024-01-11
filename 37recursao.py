"""

def reduzir_numero(numeroInt):
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1


reduzir_numero(10)"""


"""
def reduzir_numero(numeroInt):
    
    if numeroInt > 0:
        #N - 1
        reduzir_numero(numeroInt - 1)
        print(numeroInt)


reduzir_numero(5)"""


#FATORIAL SEM RECURSÃO
def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero+1):
            fatorial*= x
            return fatorial
        

print(fatorialS(4))


#FATORIAL SOLUÇÃO RECURSIVA
def fatorialR(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorialR(numero - 1)
    

print(fatorialR(4))
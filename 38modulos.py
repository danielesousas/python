#MÓDULOS SÃO OS ARQUIVOS EM PYTHON
#PACOTES SÃO DIRETÓRIOS CONTENDO CONJUNTOS DE MÓDULOS - PASTAS COM VÁRIOS ARQUIVOS EM PYTHON


#import random
#from random import choice
#import random as rd
#from random import  *
from random import (
    random,
    choice,
    randint

)

print(random())


lista = ['pedra', 'papel', 'tesoura']
print(choice(lista))
print(randint(1,5))


from pack import main, secondary

print(main.soma(1,4))
print(secondary.quadratica(200))


from pack.subdir import sub

print(sub.cubica(4))
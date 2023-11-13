"""
palpite = 9090
numero = 9


while palpite != numero:
    print("What is the correct number? ")
    palpite = int(input())
    print("Congrats, you win")


print(bool(palpite))
"""

palpite = 9
numero = 9


while True:#execucaçao sem verifcar
    print("What is the correct number? ")
    palpite = int(input())
    if palpite == numero:#verificaçao
        print("Congrats, you win")
        break
    else:
        print("Try again")
else:
print("Error")

print(bool(palpite))



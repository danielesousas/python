from random import choice

player_victory = 0
machine_victory = 0


def Option_player():
    want_player = input("Choice Stone, Paper or Scissor:")
    want_player.lower()
    if want_player == "stone":
        return want_player
    elif want_player == "paper":
        return want_player
    elif want_player == "scissor":
        return want_player
    else:
        print("Invalid option. Try again")
        Option_player()


def Option_machine():
    want_machine = choice(["stone", "paper", "scissor"])
    return want_machine


while True:

    print("-"*30)
    want_player = Option_player()
    want_machine = Option_machine()
    print("-"*30)
    
    if(want_player == "stone") and (want_machine == "scissor") \
        or (want_player == "scissor") and (want_machine == "paper") \
            or (want_player == "paper") and (want_machine == "stone"):
            #player win
            print(f"Player chose {want_player} and machine chose {want_machine}" 
            " You Win!")
            player_victory += 1

    elif (want_player == want_machine):
    #tie
        print(f"Player chose {want_player} and machine chose {want_machine}"
        " Game tied!")

    else:
        #player lose
        print("You lose!")

    print("-"*30)
    print(f"Player Victories: {player_victory}")
    print(f"Machine Victories: {machine_victory}")
    print("-"*30)

    want_player = input("Play again?")
    if want_player in ["YES", "yes", "Yes", "y", "Y"]:
        pass
    elif want_player in ["NO", "no", "No", "n", "N"]:
        break
    else:
        break
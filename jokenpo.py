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

    want_player = Option_player()
    want_machine = Option_machine()

    want_player = input("Play again?")
    if want_player in ["YES", "yes", "Yes", "y", "Y"]:
        pass
    elif want_player in ["NO", "no", "No", "n", "N"]:
        break
    else:
        break
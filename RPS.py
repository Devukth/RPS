import random
import time

print("Rock, Paper, Scissors")

options = ["Rock", "Paper", "Scissors"]
first = False
endgame = False

computerpoints = 0
playerpoints = 0

while (not endgame):
    if(not first):
        player = input("Rock, Paper, or Scissors? ")
    else:
        player = input("Rock, Paper, Scissors, or End Game? ")
        
    computer = random.choice(options)
    first = True

    # Conditions
    if (player.lower() == computer.lower()):
        print(computer, "matches", player + ". No points")

    elif (player.lower() == "rock"):
        if (computer == "Paper"):
            print(computer, "covers", player + ". Point for CPU")
            computerpoints += 1

        elif (computer == "Scissors"):
            print(player, "breaks", computer + ", Point for player")
            playerpoints += 1

    elif (player.lower() == "paper"):
        if (computer == "Rock"):
            print(player, "covers", computer + ". Point for player")
            playerpoints += 1

        elif (computer == "Scissors"):
            print(computer, "slices", player + ", Point for CPU")
            computerpoints += 1

    elif (player.lower() == "scissors"):
        if (computer == "Rock"):
            print(player, "breaks", computer + ". Point for player")
            playerpoints += 1

        elif (computer == "Paper"):
            print(computer, "covers", player + ", Point for CPU")
            computerpoints += 1

    elif (player.lower() == "end game" or player.lower() == "endgame" or player.lower() == "eg"):
        print("Player Points:", playerpoints)
        print("Computer Points:", computerpoints)
        endgame = True

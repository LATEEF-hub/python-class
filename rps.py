import random
import sys

from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
print("****************")  # header
print("*   WELCOME!!! *")
print("*      TO      *")
print("*   Rock Paper *")
print("*   Scissors   *")
print("****************")
print("")

playerchoice = input(
    "Make a choice from 1-3 to start the game:\n\n1.Rock, \n2.Paper or \n3.Scissors\n")
player = int(playerchoice)  # Casting of player input
# Validate player choice
if player < 1 or player > 3:
    sys.exit("Invalid selection! Please enter either 1, 2 or 3.")

computerchoice = random.choice("123")
computer = int(computerchoice)  # Casting of Computer input


# Result
print("")
print("You choose " + str(RPS(player)).replace("RPS.", "") + ".")
print("Python choose " + str(RPS(computer)).replace("RPS.", "") + ".")
print("")


if playerchoice == 1 and computerchoice == 3:
    print("\nCongratulations You dun chop! 😂\n")
elif playerchoice == 2 and computerchoice == 1:
    print("\nCongratulations You dun chop again baba! 😂\n")
elif playerchoice == 3 and computerchoice == 2:
    print("\nCongratulations You are a rockstar! 🎉\n")
elif playerchoice == computerchoice:
    print("\nIt's a tie! Try Again.\n")
else:
    print("🐍 Python wins!")


def playagain():
    if input("Do you want to play again? (yes/no)\n").lower() == 'y':
        return True
    else:
        return False
        while playagain():
            main()




print("")


# name = print(input("Enter your age:"))

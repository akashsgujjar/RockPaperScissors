from random import seed, randint
from random import random


def main():
    print("Akash")


if __name__ == "__main__":
    main()


def compMove():
    value = randint(1, 3)
    comp = ''
    if value == 1:
        comp = "Rock"
    if value == 2:
        comp = "Paper"
    if value == 3:
        comp = "Scissors"
    playerMove(comp)


def playerMove(comp):
    user = raw_input("Rock, Paper, or Scissors")
    gameTime(user, comp)


def gameTime(user, comp):
    if user == 'Rock' and comp == "Scissors":
        print ("User Wins")

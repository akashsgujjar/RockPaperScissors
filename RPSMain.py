from random import seed, randint
from random import random


def main():
    print("Akash")


if __name__ == "__main__":
    main()


def compMove():
    value = randint(1, 3)
    if value == 1:
        print "Computer says Rock"
    if value == 2:
        print "Computer says Paper"
    if value == 3:
        print "Computer says Scissors"


compMove()

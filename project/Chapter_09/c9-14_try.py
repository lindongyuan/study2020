from random import randint

class Die():

    def __init__(self):
        self.sides = 6

    def roll_die(self):

        print("\n这个是6面的骰子：")
        for x in range(10):
            x = randint(1,6)
            print(x)

die = Die.roll_die()

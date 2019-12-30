from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        print("The Random number within " + str(self.sides) + "：")
        for x in range(10):
            print (randint(1,self.sides))

my_sides = Die()
my_sides.roll_die()

my_sides = Die(10)
my_sides.roll_die()

my_sides = Die(20)
my_sides.roll_die()
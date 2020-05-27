#8-9 魔术师
def show_magicians(magicians):
    for magician in magicians:
        print("\nMagicians name is :" + magician)


def make_great(magicians,great_magicians):
    while magicians:
        remove_magicians ="The great " + magicians.pop()
        great_magicians.append(remove_magicians)


magicians = ['tom', 'tony', 'sam']
great_magicians = []

make_great(magicians[:],great_magicians)
print(great_magicians)
print(magicians)


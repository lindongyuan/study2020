def show_magicians(magicians):
    #打印每个魔术师的名字
    for name in magicians:
        msg = "Hello, " + name.title() + "!"
        print("\nThe old magician name is: ")
        print(msg)

def make_great(magicians,great_magicians):
    while magicians:
        magician = magicians.pop()
        great_magician = "the Great " + magician
        great_magicians.append(great_magician)

def show_magicianlis(magicians):
    for name in great_magicians:
        print("\nThe New magician name is: ")
        print(name)
        
magicians = ['cyril','david stone','Richard Mo','Eric']
great_magicians = []
show_magicians(magicians)
make_great(magicians[:],great_magicians)
show_magicianlis(magicians)
print(magicians)
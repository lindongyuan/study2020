def make_shirt(size,words):
    print("The T-shirt Size is " + size +", and the words on it are " + "\"" + words + "\"")

make_shirt(size="XXL",words="I like Python!")

def make_shirt(size,words="I love python!"):
    print("The T-shirt Size is " + size +", and the words on it are " + "\"" + words + "\"")

make_shirt("X")
make_shirt("M")
make_shirt("XXL","This is Python's word!")

def describe_city(city,country="Iceland"):
    print(city.title() + " is in " + country.title())

describe_city("reykjavik")
describe_city("Akureri")
describe_city("Hafnavyodur")

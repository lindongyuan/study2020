'''
def make_shirt(size,sest):
    print("\nThe size of this T-shirt is: " + size + ".")
    print("I need print " + sest + ".")

make_shirt('XXL','welcome')
make_shirt(sest='welcome',size='XXL')
'''

def makeshirt(size='L',sest='I love you'):
    print("\nThe size of this T-shirt is: " + size + ".")
    print("I need print: " + sest + ".")

makeshirt()
makeshirt(size='M')
makeshirt(sest='I love china')

def describe_city(city='Guangzhou',country='china'):
    print("\n" + city.title() + " is in " + country.title())

describe_city()
describe_city(city='meizhou')
describe_city(city='San Francisco',country='USA')


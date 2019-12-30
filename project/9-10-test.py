#导入全部模块
from restaurant import *
#分别导入Restaurant,IcecreamStand模块
#from restaurant import Restaurant,IcecreamStand

my_restaurant = Restaurant('ehght bowls','chinese food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(5)
my_restaurant.served_number()

my_restaurant.increment_number_served(6)
my_restaurant.served_number()
my_icecreamstand = IcecreamStand('ehght bowls','chinese food')
my_icecreamstand.show_favors()
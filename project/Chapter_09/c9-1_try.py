class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restarurant name is "+self.restaurant_name.title()+".")
        print("The restarurant's cuisine type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("The "+self.restaurant_name.title()+" is openning!")

my_restaurant = Restaurant('eight bowls','chinese food')
print(my_restaurant.restaurant_name.title())
print(my_restaurant.cuisine_type.title())
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


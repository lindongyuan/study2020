#test 9-6
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        #初始化属性restaurnt_name、cuisine_type
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())

    def open_restaurant(self):
        print("Is open:餐馆正在营业")

    def served_number(self):
        print(str(self.number_served) + " person went to the restaurant.")

    def set_number_served(self,n):
        #将就餐人数设置为n
        self.number_served = n

    def increment_number_served(self,n):
        self.number_served += n
        return self.number_served

class IcecreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['Cherry','apple','mixed']

    def show_favors(self):
        for n in self.flavors:
            print('My flavors is ' + n)
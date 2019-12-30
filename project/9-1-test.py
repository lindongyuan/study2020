#test 9-1
class Restaurant():
    '''9-1 餐馆'''
    def __init__(self,restaurant_name,cuisine_type):
        '''初始化属性restaurnt_name、cuisine_type'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())
    def open_restaurant(self):
        print("Is open:餐馆正在营业")

restaurant = Restaurant('fu','chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()


#test 9-3
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("你的姓名是：" + self.first_name.title() + " " + self.last_name.title())

    def greet_user(self):
        print("你好！" + self.first_name.title() + " " + self.last_name.title())

user_a = User('lin','dongyuan')
user_b = User('liu','feng')
user_c = User('lin','daniel')
user_a.describe_user()
user_a.greet_user()
user_b.describe_user()
user_b.greet_user()
user_c.describe_user()
user_c.greet_user()








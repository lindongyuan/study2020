'''
#test 9-4
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


my_restaurant = Restaurant('ehght bowls','chinese food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(5)
my_restaurant.served_number()

my_restaurant.increment_number_served(6)
my_restaurant.served_number()
'''
#test 9-5
class User():
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 9

    def describe_user(self):
        print("你的姓名是：" + self.first_name.title() + " " + self.last_name.title())

    def greet_user(self):
        print("你好！" + self.first_name.title() + " " + self.last_name.title())

    def increment_login_attempts(self):
        for attempts in range(5):
            attempts += self.login_attempts
            print(attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

my_user =  User('bill','clinton')
my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempts()
my_user.reset_login_attempts()
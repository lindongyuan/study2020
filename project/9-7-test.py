#test 9-7
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

class Privileges():
    def __init__(self):
        self.privileges = ['can and post','can delete post','can ban user']

    def show_privileges(self):
        print("The power of admin are:")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)

        self.privileges = Privileges()

'''
my_user =  User('bill','clinton')
my_user.describe_user()
my_user.greet_user()
my_user.increment_login_attempts()
my_user.reset_login_attempts()
'''

my_admin = Admin('Jackson','Yee')
my_admin.describe_user()
my_admin.privileges.show_privileges()
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 100

    def describe_user(self):
        print("first name: " + self.first_name)
        print("last name: " + self.last_name)
        print("age: " + str(self.age))

    def greet_user(self):
        print("Hello!" + self.first_name.title() + " " + self.last_name.title())

    def increment_login_attempts(self,):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():

    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("\n管理员有以下权限：")
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    '''显示管理员权限'''

    def __init__(self,first_name,last_name,age):

        super().__init__(first_name,last_name,age)
        self.privi = Privileges()

show_admin = Admin('Mark Elliot','Zuckerberg',22)
show_admin.greet_user()
show_admin.privi.privileges = ['can add post','can delete post','can ban usr']
show_admin.privi.show_privileges()


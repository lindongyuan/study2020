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
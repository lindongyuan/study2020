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

a = User("tim","duncon","32")
a.describe_user()
a.greet_user()
a.increment_login_attempts()
a.increment_login_attempts()
print(a.login_attempts)

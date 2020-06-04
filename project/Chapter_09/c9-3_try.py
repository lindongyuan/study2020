class User():
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("first name: " + self.first_name)
        print("last name: " + self.last_name)
        print("age: " + str(self.age))

    def greet_user(self):
        print("Hello!" + self.first_name.title() + self.last_name.title())

a = User("tim","duncon","32")
a.describe_user()
a.greet_user()

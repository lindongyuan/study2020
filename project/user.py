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
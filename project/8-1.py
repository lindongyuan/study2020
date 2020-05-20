#8.1定义函数
"""
def greet_user():
    '''显示简单的问候语'''
    print("Hello!")

greet_user()
"""
def greet_user(username):
    '''显示简单的问候语'''
    print("hello, " + username.title() + "!")

greet_user('Daniel')
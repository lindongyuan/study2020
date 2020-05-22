def greet_user(username):
    '''显示简单问候'''
    print("hello!" + username.title() + "!")

greet_user("Jesse")

def display_message(chapter):
    print("I'm learning " + chapter + " !" )

display_message("Chapter-8")


def favorite_book(title):
    print("One of my favorite books is " + title + "。")
favorite_book("Alice in wonderland")

"""
#使用while循环
def get_formatted_name(first_name,last_name):
    '''返回整个姓名'''
    full_name = first_name + " " + last_name
    return full_name.title()
#这是一个无限循环
while True:
    print("\nPlease tell me your name")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name,l_name)
    print(formatted_name)
"""

#使用退出条件
def get_formatted_name(first_name,last_name):
    full_name = first_name + " " + last_name
    return full_name
while True:
    print("\nPlease tell your name")
    print("(Enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break

    l_name = input("Last name: ")
    if l_name == "q":
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")
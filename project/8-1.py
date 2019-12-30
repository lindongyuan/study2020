'''
#8.1定义函数
#greeter.py
def greet_user(username):
    #显示简单的问候语
    print("hello," + username.title() + "!")

greet_user('jesse')
'''

'''
#8.2.1位置实参
#pets.py
def describe_pet(animal_type,pet_name):
    #显示宠物的信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster','harry')
describe_pet('dog','willie')
'''
'''
#8.2.2关键字实参
#pets.py
def describe_pet(pet_name,animal_type):
    #显示宠物的信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#位置实参的顺序很重要，函数参数位置调换后，位置参数调用出现荒谬结果
describe_pet('dog','willie')
#关键字实参的调用方法
describe_pet(animal_type='hamster',pet_name='harry')

#8.2.3默认值
#pets.py
def describe_pet(pet_name,animal_type='dog'):
    #显示宠物的信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#同以上函数调用结果相同，在函数调用中只提供小狗的名字：
describe_pet('willie')
describe_pet(pet_name='harry',animal_type='hamster')
'''
def describe_pet(animal_type,pet_name):
    #显示宠物的信息
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet()
class Dog():
    #简单模拟DOG
    def __init__(self,name,age):
        '''初始化属性'''
        self.name = name
        self.age = age

    def sit(self):
        '''蹲下'''
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        '''打滚'''
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie',6)
your_dog = Dog('lucy',3)

print("My dog's nanme is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " year old.")
your_dog.roll_over()
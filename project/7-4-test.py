#编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit'时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
'''
message = "please enter the ingredients fo pizza:"
pisas = ""
while pisas != 'quit':
    pisas = input(message)
    if pisas != 'quit':
        print("We'll add "+pisas+" to pizza.")


message = "please enter the ingredients fo pizza:"
active = True
while active:
    pisas = input(message)
    if pisas == 'quit':
        active = False
    else:
        print("We'll add "+pisas+" to pizza.")
'''

message = "Please enter the age"
message += "\nHow old are you?"

while True:
    age = input(message)
    #age = int(age)
    if age == quit:
    elif int(age) < 3:
        print("is free")
    elif int(age) <= 12:
        print("The ticket is $10 ")
    else:
        print("The ticket is $15")
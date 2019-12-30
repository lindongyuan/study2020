'''
current_number = 1
while current_number <=5:
    print(current_number)
    current_number +=1

#7-2-2：让用户选择何时退出
prompt = "\tTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    #print(message)
    #当输入quit时，不显示输入的信息
    if message != 'quit':
        print(message)

#7-2-3：使用标志
prompt = "Tell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)



#7-2-4：使用break退出循环
prompt = "Tell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to "+city.title()+"!")

'''

#7-2-5：在循环中使用continue
#counting.py
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
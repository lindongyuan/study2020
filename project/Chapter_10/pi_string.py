filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

while pi_string:
    birthday = input("请输入你的生日，格式是（月日年）：")
    if birthday in pi_string:
        print("你的生日包含在PI表里")
    else:
        print("你的生日没有包含在PI表里")
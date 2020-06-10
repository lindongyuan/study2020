filename = "guest.txt"

while True:
    names = input("请输入你的用户名： ")
    print("welcome back：" + names + ".")
    with open(filename,'a') as file_object:
        file_object.write(names + " Logging.\n")

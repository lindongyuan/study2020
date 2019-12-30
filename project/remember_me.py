import json
'''
username = input("What is your name?")
filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back, " + username + "!")

#如果以前存储了用户名，就加载它
#否则，就提示用户输入用户名并存储它
#合并存入Json,读取json
filename =  'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remeber you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")


#写成函数
def green_user():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is you name? ")
        with open(filename,'w') as f_obj:
            json.dump(username,f_obj)
            print("We'll remeber you when you come back, " + username + "!")
    else:
        print("Welcome back, " + username + "!")

green_user()
'''
#重构函数
def get_stored_username():
    #如果存储了用户名，就获取它
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is you name?")
    filename = 'username.json'
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
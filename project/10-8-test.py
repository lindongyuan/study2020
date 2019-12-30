def pet(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.readlines()
    except FileNotFoundError:
        pass
        #print("找不到文件")
    else:
        for content in contents:
            print(content.rstrip())

'''
filename = 'dogs.txt'
pet(filename)
print("---------------`1")
filename = 'cats.txt'
pet(filename)
print("---------------`1")
'''
filename = 'error.txt'
pet(filename)
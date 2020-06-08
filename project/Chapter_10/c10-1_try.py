file_name = "learning_python.txt"
'''
#打印整个文件
with open(file_name) as file_object:
    lines = file_object.read()

print(lines)

#遍历文件对象
with open(file_name) as file_object:
    for line in file_object:
        print(line)
'''
#将各行存入至列表中
contents = ''
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    contents += line.strip()

print(contents)
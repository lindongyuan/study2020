filename = 'inpython.txt'
#第一次打印整个文件
print('第一次打印:')
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
    print('---------------------')

#第二次打印遍历整个文件
print('第二次打印:')
with open(filename) as file_object:
    for line in file_object:

        print(line.rstrip())

#第三次打印时将各行存储在一个列表中，再在 with 代码块外打印它们
print('第三次打印:')
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
filename = 'inpython.txt'
with open(filename) as file_object:
    contents = file_object.readlines()

for content in contents:
    content = content.replace('Python','c')
    print(content.title())
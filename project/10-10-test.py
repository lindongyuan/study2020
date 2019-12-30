filename = 'pg10.txt'

while True:
    with open(filename) as file_object:
        text = input('请输入需要检测的单词：')
        if text == 'q':
            break
        else:
            contents = file_object.read()
            words = contents.lower().split().count(text)
            print("该单词 " + "\'" + text + "\'" + " 在这篇文章出现的次数是:" + str(words))
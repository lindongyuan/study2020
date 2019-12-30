def count_words(filename):
    '''计算一个文件大致包含多少个单词'''
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        #pass
        msg = "Sorry,the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

#统计单个文件单词数量
filename = 'alice.txt'
count_words(filename)

#使用循环统计多个文件单词数量
filenames = ['alice.txt','siddhartha.txt','moby_dict.txt','little_women.txt']
for filename in filenames:
    count_words(filename)
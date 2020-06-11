def count_words(filename):
    '''计算一个文件大致包含多少个单词'''
    try:
        with open(filename) as f_object:
            contents = f_object.read()
    except FileNotFoundError:
        msg = "Sorry,the file " + filename + " does not exst."
        print(msg)
    except UnicodeDecodeError:
        msg = "Sorry,The file " + filename + " Code by GBK."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename +" has about " + str(num_words) + " words.")

'''
filename = "Moby Dick.txt"
count_words(filename)
'''

filenames = ['Alice in wonderland.txt','Moby Dick.txt','siddhartha.txt','The Little Warrior.txt']
for filename in filenames:
    count_words(filename)

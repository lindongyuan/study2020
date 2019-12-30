from collections import OrderedDict

favorite_language = OrderedDict()

favorite_language['jen'] = 'python'
favorite_language['sarah'] = 'c'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'

print("这些Key有：")
for key in favorite_language.keys():
    print(key.title())

print("这些Value有：")
for value in set(favorite_language.values()):
    print(value.title())

'''
favorite_language = {'jen':'python',
                     'sarah':'c',
                     'edward':'ruby',
                     'phil':'python',}

print("这些KEY有：")
for key in favorite_language.keys():
    print(key)

print("这些Value有：")
for value in set(favorite_language.values()):
    print(value)

#创建一个字典，在其中存储三条大河流及流经的国家
rivers = {'nile':'Egypt',
          'Amazon':'Brazil',
          'Yangtze':'China',}

for river,key in rivers.items():
    print("The "+river.title() +" runs through "+ key.title()+".")

#使用循环将字典中的每条河流的名字都打印出来
print("世界三大河流是：")
for key in rivers.keys():
    print(key)

#使用循环将字典中名含的每个国家的名字都打印出来
print("这些河流流经的国家都有：")
for value in rivers.values():
    print(value)
'''
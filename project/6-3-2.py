'''
favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',

}

friends = ['phil','sarah']

for name in sorted(favorite_languages.keys()):
    print(name.title())

    if name in friends:
        print("HI "+name.title()+
              ",I see your favortitle language is "+
              favorite_languages[name].title()+"!")

if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll!")



#按顺序遍历字典中的所有键 sorted()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

'''
#遍历字典中所有的值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for values in favorite_languages.values():
    print(values)

for values in sorted(set(favorite_languages.values())):
    print(values)
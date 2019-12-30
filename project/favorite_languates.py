from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

'''
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}



for name,languages in favorite_languages.items():
    print("\n"+ name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t"+language.title())
'''

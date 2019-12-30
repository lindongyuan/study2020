'''
name1 = {'first':'albert',
         'last':'einstein',
         'age':27,
         'city':'princeton',
         }

name2 = {'first':'marie',
         'last':'curie',
         'age':32,
         'city':'paris',
         }

name3 = {
    'first':'Lin',
    'last':'Dongyuan',
    'age':'37',
    'city':'meizhou',
}

users = [name1,name2,name3]

for user in users:
    fullname = user['first']+' '+user['last']
    print (fullname+"，他今年已经"+str(user['age'])+"岁了，住在"+user['city'])

favorite_places = {'abert':['madrid','amsterdam'],
                   'marie':['berlin','paris'],
                   'dongyuan':['hangzhou','dali'],}

for key,volue in favorite_places.items():
    print(key.title()+"喜欢旅游的地方有：")
    for city in volue:
        print("\t"+city.title())
'''
number = {
    'Tony':[3,5,9],
    'danny':[8,7,5],
    'yifan':[6,1],
    'kin':[5,6,2,9],
}

for nam,nums in number.items():
    print(nam.title()+"喜欢的数字有：")
    for num in nums:
        print("\t"+str(num))

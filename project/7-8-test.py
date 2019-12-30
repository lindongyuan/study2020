'''
#7-8 创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名字；再创建一个名为 finished_sandwiches的空列表。
#遍历列表 sandwich_orders，对于其中的每种三明治，都打印一条消息，如 I made your tuna sandwich，并将其移到列表finished_sandwiches。
#所有三明治都制作好后，打印一条消息，将这些三明治列出来。

sandwich_orders = ['Tuna','Chicken','Baconic','Beef','pastrami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your "+ sandwich +" sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThese sandwicher have done:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)


#7-9 五香烟熏牛肉（pastrami）卖完了：使用为完成练习 7-8 而创建的列表sandwich_orders，并确保'pastrami'在其中至少出现了三次。
#在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个 while循环将列表 sandwich_orders
#中的'pastrami'都删除。确认最终的列表 finished_sandwiches 中不包含'pastrami'。
sandwich_orders = ['Tuna','Chicken','Baconic','Beef','pastrami','pastrami','pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print('Sorry,The pastrami has been sold!')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your "+ sandwich +" sandwich.")
    finished_sandwiches.append(sandwich)

print("\nThese sandwicher have done:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

'''
#7-10 梦想的度假胜地：编写一个程序，调查用户梦想的度假胜地。使用类似于“Ifyou could visit one place in the world,
#where would you go?”的提示，并编写一个打印调查结果的代码块。

places = {}
polling_active = True
while polling_active:
    name = input('Tell me your name: ')
    place = input('If you could visit one place in the World,where yould you go?')
    places[name] = place
    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == "no":
        polling_active = False


print('---- Everyone likes to go. ----')
for name,place in places.items():
    print(name + ' like is: '+place)


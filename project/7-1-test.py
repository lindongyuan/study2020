'''
#test:7-1
rent = input("你想租什么车？ ")
print("Let me see if Ican find you a "+rent.title())


#test:7-2
meals = input("请问有几个人用餐？ ")
meals = int(meals)
if meals >= 8:
    print("不好意思，目前暂时没有适合的座位")
else:
    print("麻烦就座吧！")

'''

#test:7-3
number =  input("请输入数字： ")
number = int(number)
if number % 10 == 0:
    print("这个是整数！")
else:
    print("这个不是整数！")

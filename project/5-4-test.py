"""
注释开始
usernames=['admin','eric','daniel','dylan','tony']
for username in usernames:
    if username=="admin":
        print("Hello "+username+",would you like to see a status report?")
    else:
        print("hello, " + username +",thank you for logging in again")

usernames=[]
if usernames:
    for username in usernames:
        print("hello, " + username + ",thank you for logging in again")
else:
    print("We need to find some users!")
注释结束
"""

current_users=['admin','eric','daniel','dylan','tony']
new_users=['pony','eric','Daniel','andy','wang']
for new_user in new_users:
    if new_user.lower() in [temp_user.lower() for temp_user in current_users]:
        print(new_user+"不能使用,请录入其他用户名")
    else:
        print(new_user+"，恭喜，可以使用！")
print("\n比较结束")

numbers = list(range(1,10))
for num in numbers:
    if num == 1:
        print('%dst'%num)
    elif num == 2:
        print('%dnd'%num)
    elif num == 3:
        print('%drd'%num)
    else:
        print('%dth'%num)


def build_profile(first,last,**user_info):
    #创建一个字典，其中包含我们知道的有关用户的一切
    #形参**user_info中的两个星号让Python创建一个名为user_info的空字典
    profile = {}
    #在build_profile()的函数体内，我们创建了一个名为profile的空字典
    profile['first_name'] = first
    profile['last_name'] = last
    #我们遍历字典user_info中的键—值对，并将每个键—值对都加入到字典profile中
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
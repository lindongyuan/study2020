
#test:8-12
'''
def sandwich_make(*toppings):
    #制作三文治
    print("\nMaking a swndwich with the floowing topppings:")
    for topping in toppings:
        print("- " +topping)

sandwich_make('buns','meat','cheest')
sandwich_make('buns','mayo','lettuce','tomato')
sandwich_make('turkey','lettuce','tomato')

'''
#test:8-13
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)
user_profile = build_profile('lin','dongyuan',location='meizhou',field='')
print(user_profile)


def make_cars(brand,model,**car_info):
    profile = {}
    profile['brand_name'] = brand
    profile['model_name'] = model
    for key,value in car_info.items():
        profile[key] = value
    return  profile

car = make_cars('subaru', 'outback', color='blue', tow_package=True)
print(car)


def make_car(manufacturer,model,**car_info):
    profile = {}
    profile['car_manufacturer'] = manufacturer
    profile['car_model'] = model
    for key,value in car_info.items():
        profile[key] = value
    return profile

car_sub = make_car('subaru','outback',color='blue',two_package=True)
print(car_sub)


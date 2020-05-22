"""
def describe_pet(animal_type,pet_name):
    print("\nI have a " +  animal_type + ".")
    print("My " + animal_type + " 's name is " + pet_name.title() + ".")

#位置实参
describe_pet("hamster","harry")
describe_pet("dog","Willie")

#关键字实参
describe_pet(animal_type="hamster",pet_name="harry")
describe_pet(pet_name="Willie",animal_type="dog")
"""
#指定默认值
#注意形参位置
def describe_pet(pet_name,animal_type='dog'):
    print("\nI have a " +  animal_type + ".")
    print("My " + animal_type + " 's name is " + pet_name.title() + ".")

#describe_pet(pet_name="Willie")
#willie Dog
describe_pet("Willie")
describe_pet(pet_name="Willie")
#Harry hamster
describe_pet("harry","hamster")
describe_pet(pet_name="harry",animal_type="hamster")
describe_pet(animal_type="hamster",pet_name="harry")
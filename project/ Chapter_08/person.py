def build_person(first_name,last_name):
    person = {"first":first_name,"last":last_name}
    return person
musician = build_person("jimi","hendrix")
print(musician)

#扩展函数，接受可选值
def build_person(first_name,last_name,age=""):
    person = {"first":first_name,"last":last_name}
    if age:
        person["age"] = age
    return person
masician = build_person("jimi","hendrix",age=27)
print(masician)
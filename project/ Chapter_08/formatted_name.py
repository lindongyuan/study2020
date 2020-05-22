def get_formatted_name(first_name,last_name):
    #返回完整姓名
    full_name = first_name + " " + last_name
    return full_name.title()

musician = get_formatted_name("jimi","hendrix")
print(musician)

def get_formatted_name(first_name,middle_name,last_name):
    #返回完整姓名
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

musician = get_formatted_name("join","lee","hooker")
print(musician)

#middle_name默认为空
def get_formatted_name(first_name,last_name,middle_name=""):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name

    return full_name.title()
musician = get_formatted_name("jimi","hendrix")
print(musician)

musician = get_formatted_name("john","hooker","lee")
print(musician)
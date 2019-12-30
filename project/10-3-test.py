filename = 'guest.txt'
with open(filename,'w') as file_object:
    message = "Please enter your name:"
    file_object.write(input(message))


filename = 'guest_book.txt'

while True:
    with open(filename,'a') as file_object:
        message = "\nPlease enter your name:"
        message += "\n(Enter 'exit' to quit!)"
        file_content = input(message)
        if file_content ==  'exit':
            break
        else:
            file_object.write(file_content + " is login.\n")
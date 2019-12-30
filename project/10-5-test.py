filename = 'reasons.txt'

while True:
    message = "\nPlease enter why you like programming:"
    message += "\n(Enter 'exit' to quit!):"
    reason = input(message)
    if reason == 'exit':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write(reason + "\n")
while True:
    first_number = input("Please enter first number:")
    if first_number == 'q':
        break
    second_number = input('Please enter second number:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Type error")
    else:
        print(answer)
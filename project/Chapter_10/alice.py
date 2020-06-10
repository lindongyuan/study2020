file_name = "alice.txt"

try:
    with open(file_name) as file_object:
        contents = file_object.read()
        print(contents)
except FileNotFoundError:
    msg = "Sorry,The file " + file_name + " does not exist."
    print(msg)
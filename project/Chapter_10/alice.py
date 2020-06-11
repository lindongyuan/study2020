file_name = "Alice in wonderland.txt"

try:
    with open(file_name) as file_object:
        contents = file_object.read()
        #print(contents)
except FileNotFoundError:
    msg = "Sorry,The file " + file_name + " does not exist."
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + file_name + " has about " + str(num_words) + " words.")
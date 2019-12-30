filename = 'pi_digits.txt'
filename2 = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

with open(filename2) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input ("Enter your birthday,in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appers in the first millon digits of pi!")
else:
    print("Your birthday does not appers in the first millon digits of pi.")
'''
print(pi_string[:52] + "...")
print(len(pi_string))
'''
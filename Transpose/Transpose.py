#
# Bryce Benson
# COMP 163
# 10/6/21
# Transpose
#



dict_size = int(input("Enter how many letter you want to encrypt:"))
transposition_size = int(input("Enter the transposition size:"))
count = 0
dict_transpose = {}

while count >= 0 and count < dict_size:
# Checks if the count variable is greater than 0 and less than the size_transpoet variable
    key = input("Enter a letter:")
    if len(key) != 1:
    # If the legnth of the key is not 1, then you need to enter another value for the key
        print("You must enter 1 letter")
    else:
        value = input("Enter a code for a letter:")
        if len(value) != transposition_size:
        # If the legnth of the value is not the transposition size, then the loops goes back to the begining
            print("code must be as long as the transposition size")
        elif key == value:
        # If the key legnth is equal to the size of the value legnth, then the loops goes back to the begining
            print("The letter and code for the letter have to be different")
        else:
            key = key.lower()
            dict_transpose[key] = value
            count +=1

message = input("Type the message to transpose:")
message = message.lower()
for i in dict_transpose.keys():
#This replaces the keys in the message with the values.
    message = message.replace(i,dict_transpose[i])
print(message)
encode = input("Type in the transpositon of the message:")

if message == encode:
#Checks if what you type for encode is the transposition of the message
    print("Access granted")
else:
    print("Denied!")
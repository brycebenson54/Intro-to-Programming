#
#Bryce Benson
#COMP 163
# 10/6/21
# Transposition
#

my_dict = {}
play = input("Enter the name of the play:")
transposition_size = int(input("Enter the transposition size:"))
count = 0

new_play = "".join(set(play))
for j in new_play:
    encode = input(f"Encrypt value for {new_play[count]}:")
    while count < len(new_play):
      if len(encode) != transposition_size:
      # if the legnth of variable encode is not equal to variable transposition_size, it will keep asking you to input a variable the legnth is equal to transposition size
        encode = input((f"Value must be {transposition_size} characters long:"))

      elif encode in my_dict.values():
    # if variable encode is in the value of the dictionary, it will ask you to put a different input
        encode = input(("Values for each letter must be different:"))
      else:
        my_dict[j] = encode
        count +=1
        break
for i in my_dict.keys():
#This replaces the keys in the message with the values.
    play = play.replace(i,my_dict[i])
print(f"Transposition is {play}")

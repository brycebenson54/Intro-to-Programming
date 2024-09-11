#
#Bryce Benson
#COMP 163
# 10/21/21
# Registration Line
#


reg_line = {}
reg_numlist = []
frustration_list = []
doLoop = True

while doLoop:
# Runs program as long as doLoop is True.
    n = int(input("How many students are registered for the next semester?"))
    while n < 3:
    # Keeps asking the user how many students are registered for next semester until n is at least 3.
        print("There must be a minimum of 3 students registered.")
        n = int(input("How many students are registered for the next semester?"))
    count = 1
    for i in range(n+1):
       if count <= n:
        # Asks user for registration number if count is less than or equal to n.
            reg_num = int(input(f"What is student {count}'s registration number?"))
            while reg_num < -1000000000 or reg_num > 1000000000:
            #If reg_num is greater than 1 billion or less than negative 1 billion, then the program will keep asking user to input registration numbers.
                print("Invalid Registration Number")
                reg_num = int(input(f"What is student {i}'s registration number?"))
            else:
                reg_line[count] = reg_num
                count +=1
    for i in reg_line.values():
    #Puts every value in the dictionary to the list reg_numlist
        reg_numlist.append(i)
    reg_numlist.sort()
    count = 1
    break

count = 0

for i in reg_numlist:
# Every element in the list reg_numlist,besides the first and last element, the frustration will be calculated and put into the list frustration_list.
    if i == reg_numlist[0]:
    # If i is the first element in list reg_numlist, increment variable count by 1.
        count += 1
    elif i == reg_numlist[-1]:
    # if i is the last element of the list, stop the while loop doLoop.
        break
    else:
        left_area = (reg_numlist[count-1]+i)/2
        right_area = (reg_numlist[count+1]+i)/2
        frustration_area = right_area - left_area
        frustration_list.append(frustration_area)
        count +=1

print(f"The smallest area of frustration is {min(frustration_list)}")
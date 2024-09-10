#
#Bryce Benson
#COMP 163
# 12/2/21
# Gradebook
#

import csv
from Gradebook1 import List


with open ("C:\\Users\\nisel\\Downloads\\Grades.csv","r") as csvfile:         
    grade_reader = csv.reader(csvfile, delimiter=',')
    avg = 0
    class_list = []
    males_list = []
    females_list = []
    average_list = []
    student_list = []
    print("Name        Average")
    for row in grade_reader:
    # Iterates through each row in the Grades.csv file
        class_list = (row[2:])
        if "Grade 1" in row:
            pass
        else:
        # This skips the first row in Grades.csv so I work with purly numbers
            avg = List.average(class_list)
            print(f"{row[0]}   {avg:.2f}")
            if "M" in row[1]:
            # Checks to see if the student in that row is a male
                males_list.append(avg)
            if "F" in row[1]:
            # Checks to see if the student in that row is a female
                females_list.append(avg)
            average_list.append(avg)
            student_list.append(row[0])
    print(f"\nMales       {List.average(males_list):.2f}")
    print(f"Females     {List.average(females_list):.2f}")
    print(f"\nClass       {List.average(average_list):.2f}")
    print(f"\n{student_list[average_list.index(max(average_list))]} was the highest with an average of {max(average_list)}")

#
#Bryce Benson
#COMP 163
# 12/2/21
# Gradebook
#

import csv

class List():
    def __init__(self):
        self.class_list = []
    def average(self, class_list)


with open ("C:\\Users\\nisel\\Downloads\\Grades.csv","r") as csvfile:         
    grade_reader = csv.reader(csvfile, delimiter=',')
    count = 2
    average = 0
    class_avg = 0
    class_list = []
    for i in grade_reader:
        if "Grade 1" not in i:
            class_list = i[2:-1]
            for j in class_list:
                j = float(j)
                average += j
            average = average/5
            print(average)